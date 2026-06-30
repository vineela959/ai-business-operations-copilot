import { useEffect, useState } from "react";
import { UploadCloud, FileText, Trash2 } from "lucide-react";
import { deleteDocument } from "../services/api";

function DocumentsPanel() {
  const [file, setFile] = useState(null);
  const [documents, setDocuments] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  async function loadDocuments() {
    const token = localStorage.getItem("token");

    const response = await fetch("http://127.0.0.1:8000/documents/", {
      headers: { Authorization: `Bearer ${token}` },
    });

    const data = await response.json();
    setDocuments(data);
  }

  useEffect(() => {
    loadDocuments();
  }, []);

  async function handleUpload() {
    if (!file) return;

    setUploading(true);
    setMessage("");

    const token = localStorage.getItem("token");
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/documents/upload", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
      body: formData,
    });

    if (response.ok) {
      setMessage("✅ Document uploaded successfully");
      setFile(null);
      loadDocuments();
    } else {
      setMessage("❌ Upload failed");
    }

    setUploading(false);
  }

  async function handleDelete(documentId) {
    await deleteDocument(documentId);
    setMessage("🗑️ Document deleted");
    loadDocuments();
  }

  return (
    <section className="activity-card">
      <div className="documents-header">
        <div>
          <h3>Knowledge Base</h3>
          <p>{documents.length} document(s) indexed</p>
        </div>

        <UploadCloud size={26} />
      </div>

      <div className="upload-box">
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {file && (
          <div className="selected-file">
            <FileText size={18} />

            <div>
              <strong>{file.name}</strong>
              <p>{(file.size / 1024).toFixed(1)} KB</p>
            </div>
          </div>
        )}

        <button onClick={handleUpload} disabled={uploading}>
          {uploading ? "Uploading..." : "Upload Document"}
        </button>

        {message && <div className="upload-message">{message}</div>}
      </div>

      <div className="document-list">
        {documents.map((doc) => (
          <div key={doc.id} className="document-item">
            <FileText size={18} />

            <div className="document-info">
              <strong>{doc.filename}</strong>
              <span>ID #{doc.id}</span>
            </div>

            <Trash2
              size={18}
              className="delete-icon"
              onClick={() => handleDelete(doc.id)}
            />
          </div>
        ))}
      </div>
    </section>
  );
}

export default DocumentsPanel;