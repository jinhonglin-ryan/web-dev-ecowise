import React from 'react';
import Map from './Map';
import { useJsApiLoader } from '@react-google-maps/api';
import { mapOptions } from './MapConfiguration';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import '../App.css';

function MyHtmlComponent() {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: mapOptions.googleMapApiKey
  });

  return (
    <div style={{ position: 'relative', height: '100vh' }}>
      {isLoaded ? <Map /> : <div>Loading...</div>}

      <nav class="nav flex-column custom-nav d-flex align-items-center justify-content-center" style={{ position: 'absolute', top: 0, zIndex: 2 }}>
        <a class="nav-link active" aria-current="page" href="http://localhost:3000/main">Why Us</a>
        <a class="nav-link active" aria-current="page" href="http://localhost:3000/main">Chat</a>
        <a class="nav-link active" aria-current="page" href="http://localhost:3000/map">Game</a>
        <a class="nav-link active" aria-current="page" href="#">Rank</a>
        <a class="nav-link active" aria-current="page" href="#">Contact</a>
      </nav>
    </div>
  );
}

export default MyHtmlComponent;
