import React from 'react';
import Map from './Map';
import { useJsApiLoader } from '@react-google-maps/api';
import { mapOptions } from './MapConfiguration';
import './FullPageMapWithNav.css'; // Import your stylesheet

function FullPageMapWithNav() {
  const { isLoaded } = useJsApiLoader({
    id: mapOptions.googleMapApiKey,
    googleMapsApiKey: mapOptions.googleMapApiKey
  });

  return (
    <div className="full-page-container">
      <div className="map-container">
        <Map isLoaded={isLoaded}/>
      </div>

      <div className="info-box">
        {/* Insert your recorded messages here */}
        At the core of our mission at Georgetown University is an unwavering commitment to student-centered advocacy,
          emphasizing the critical importance of energy conservation and environmental protection.
          We firmly believe in the power of empowering our youth,
          recognizing their pivotal role in forging a more sustainable and environmentally conscious future.
      </div>

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

export default FullPageMapWithNav;


