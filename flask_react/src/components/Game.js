import React, { useState } from 'react';
import axios from 'axios';
import './FullPageMapWithNav.css'; // Import your stylesheet

function ImageUploadComponent({ onModeChange, setTextResponse }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imageURL, setImageURL] = useState('');

  const selectFileHandler = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setImageURL(URL.createObjectURL(file)); // Generate a URL for preview
    }
  };

  const uploadHandler = async () => {
    if (!selectedFile) {
      console.log('No file selected.');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedFile); // Append the file with key 'image'
    const username = localStorage.getItem('username');
    if (username) {
        formData.append('username', username); // Append username to form data
    }
    try {
      const response = await axios.post('/image_upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      // The response should contain the text returned from analyzing the image
      setTextResponse(response.data.response); // Update the parent component with the response
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div>
      <div className="upload-container">
        <input type="file" id="file" className="upload-input" onChange={selectFileHandler} />
        <label htmlFor="file" className="upload-label">Drag your file here or click to select</label>
        <button onClick={uploadHandler} className="upload-btn">Upload</button>
      </div>

      {imageURL && (
        <div>
          <img src={imageURL} alt="Uploaded" style={{ maxWidth: '500px', maxHeight: '500px' }} />
          <div>
            <a href="http://localhost:3000/game" className="btn btn-primary" onClick={() => onModeChange('game')}>Game</a>

            <button onClick={() => onModeChange('chat')}>Chat</button>
          </div>
        </div>
      )}



      <nav className="nav flex-column custom-nav" style={{
        position: 'absolute',
        top: '50%',
        left: '0',
        transform: 'translateY(-50%)',
        height: '100%', // Take full height to align items in the middle
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center', // This centers the links vertically
        zIndex: 2
        }}>
        <a href="http://10.150.243.90:3000/whyus">Why Us</a>
        <a href="http://localhost:3000/main">Chat</a>
        <a href="http://10.150.243.90:3000/game">Game</a>
        <a href="http://10.150.243.90:3000/rank">Rank</a>
        <a href="#">Contact</a>
      </nav>
    </div>
  );
}

export default ImageUploadComponent;