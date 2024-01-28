import { GoogleMap, useLoadScript, Marker, InfoWindow } from '@react-google-maps/api';
import first from "../assets/images/first.png"
import second from "../assets/images/second.png"
import third from "../assets/images/third.png"
import others from "../assets/images/others.png"
import { useState } from 'react';
import { mapOptions } from './MapConfiguration';

const Map = (props) =>{

    const {isLoaded} = props;
    const [selectedMarker, setSelectedMarker] = useState("");
    const containerStyle = {
        width: '100vw', // 400px
        height: '100vh', //400 px
    };
      
    const center = {
        lat: 38.907852,
        lng: -77.072807
    };

    const markers = [
        {
            name:"College of Arts & Sciences",
            rank: 1,
            location: {
                lat:38.90696674360298,
                lng: -77.07451376430606
            }
        },
        {
            name:"Georgetown Law",
            rank: 2,
            location: {
                lat:38.906503838541575, 
                lng: -77.07228699210988
            }
        },
        {
            name:"McCourt School of Public Policy",
            rank: 3,
            location: {
                lat:38.90759345535584,
                lng: -77.0733079285246
            }
        },
        {
            name:"McDonough School of Business",
            rank: 4,
            location: {
                lat:38.9071152769573,
                lng:  -77.07276389377685
            }
        },
        {
            name:"School of Medicine",
            rank: 5,
            location: {
                lat:38.907235568546575, 
                lng:  -77.07515469718749
            }
        },
        {
            name:"School of Nursing",
            rank: 6,
            location: {
                lat:38.908008017339604, 
                lng: -77.07425990406992
            }
        },
        {
            name:"School of Health",
            rank: 7,
            location: {
                lat:38.9087158280195, 
                lng: -77.07349956436336
            }
        },
    ]
    return isLoaded && (
        <>
            <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={17.5}
            options={{
                disableDefaultUI: true,
                styles: mapOptions.mapTheme
            }}
            >
                {markers.map((marker)=>{
                    return (
                        <div key = {marker.name}>
                            <Marker 
                                position = {marker.location}
                                options = {{
                                    icon: 
                                    marker.rank === 1 
                                    ? {url: first, scaledSize: new window.google.maps.Size(100, 100)}:marker.rank=== 2
                                    ? {url: second, scaledSize: new window.google.maps.Size(90, 90)}:marker.rank===3
                                    ? {url: third, scaledSize: new window.google.maps.Size(80, 80)}:
                                    {url:others,scaledSize: new window.google.maps.Size(100, 100)},
                                }}
                                onClick={()=>{
                                    setSelectedMarker(marker);
                                }}
                            />
                        </div>
                    )
                })}
                {
                    selectedMarker &&
                    (<InfoWindow 
                        position={selectedMarker.location}
                        options={{
                            pixelOffset: new window.google.maps.Size(0, -40)
                        }}
                    >
                        <div>
                            <h1>{selectedMarker.name}</h1>
                            <h1>Rank: {selectedMarker.rank}</h1>

                            <button onClick={()=>{
                                setSelectedMarker("");
                            }}>Close</button>
                        </div>
                    </InfoWindow>)
                }
            </GoogleMap>
        </>
    )
}

export default Map