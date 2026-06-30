from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.repositories.customer_repository import CustomerRepository
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_customer = CustomerRepository.get_by_email(db, customer.email)

    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer with this email already exists")

    return CustomerRepository.create(db, customer)


@router.get("/", response_model=list[CustomerResponse])
def get_customers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return CustomerRepository.get_all(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    customer = CustomerRepository.get_by_id(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer_data: CustomerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    customer = CustomerRepository.get_by_id(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    existing_customer = CustomerRepository.get_by_email(db, customer_data.email)

    if existing_customer and existing_customer.id != customer_id:
        raise HTTPException(status_code=400, detail="Email already used by another customer")

    for key, value in customer_data.model_dump().items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)

    return customer


@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    customer = CustomerRepository.get_by_id(db, customer_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    CustomerRepository.delete(db, customer)

    return {"message": "Customer deleted successfully"}