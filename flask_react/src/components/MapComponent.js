import React from 'react';
import Map from './Map'; // Your Map component
import { useJsApiLoader } from '@react-google-maps/api';
import { mapOptions } from './MapConfiguration';

function FullPageMapWithNav() {
  const { isLoaded } = useJsApiLoader({
    id: mapOptions.googleMapApiKey,
    googleMapsApiKey: mapOptions.googleMapApiKey
  });

  const mapContainerStyle = {
    width: '100%', // 100% of the viewport width
    height: '100%', // 100% of the viewport height
    position: 'fixed',
    top: 0,
    left: 0,
    zIndex: 0 // Make sure it's behind the navbar
  };

  return (
    <div style={{ position: 'relative', width: '100vw', height: '100vh' }}>

      <div className="MapComponent" style={mapContainerStyle}>
        <Map isLoaded={isLoaded}/>
      </div>

      {/* Navigation bar */}
      <nav className="nav flex-column custom-nav d-flex align-items-center justify-content-center" style={{ position: 'absolute', top: '50%', left: '8%', transform: 'translate(-50%, -50%)', zIndex: 2 }}>
        <a className="nav-link active" aria-current="page" href="http://localhost:3000/main">Why Us</a>
        <a className="nav-link active" aria-current="page" href="http://localhost:3000/main">Chat</a>
        <a className="nav-link active" aria-current="page" href="http://localhost:3000/map">Game</a>
        <a className="nav-link active" aria-current="page" href="#">Rank</a>
        <a className="nav-link active" aria-current="page" href="#">Contact</a>
      </nav>

    </div>
  );
}

export default FullPageMapWithNav;

