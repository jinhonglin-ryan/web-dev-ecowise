import React, { useState } from 'react';
import axios from 'axios';

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
      <input type="file" onChange={selectFileHandler} />
      <button onClick={uploadHandler}>Upload</button>

      {imageURL && (
        <div>
          <img src={imageURL} alt="Uploaded" style={{ maxWidth: '300px', maxHeight: '300px' }} />
          <div>
            <button onClick={() => onModeChange('game')}>Game</button>
            <button onClick={() => onModeChange('chat')}>Chat</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default ImageUploadComponent;
