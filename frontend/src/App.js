import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const App = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setPrediction(null);
    setError(null);
  };

    const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post("http://localhost:8000/uploadfile/", formData);
      setPrediction(response.data.resposta);
      setError(null);
    } catch (error) {
      setError("Erro");
    }
  };


  return (
    <div className="container">
          <h1 className="titulo">Upload Captcha Numerico</h1>
          <form onSubmit={handleSubmit} className="formulario">
            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              className="input-arquivo"
            />
            <button type="submit" className="botao">
              Submit
            </button>
          </form>

          {/* usa estruturas condicionais para exibir certas coisas apenas se: */}
          {prediction !== null && (
            <div className="resultado">
              <p className="texto-resultado">{prediction}</p>
            </div>
          )}

          {error && (
            <div className="erro">
              <p className="texto-erro">{error}</p>
            </div>
          )}
    </div>
  );
};

export default App;
