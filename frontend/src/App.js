import * as React from 'react';
import { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import Map, { Marker, FullscreenControl, GeolocateControl, NavigationControl, Popup } from 'react-map-gl';
import { Sidebar, CustomFlowbiteTheme } from 'flowbite-react';
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser } from 'react-icons/hi';

import 'mapbox-gl/dist/mapbox-gl.css';

const MAPBOX_TOKEN = 'pk.eyJ1Ijoic2FudGFrYXVzIiwiYSI6ImNsd255azRteDE2b2cyam83YmlocmZxYzUifQ.YYF8_g3GceatHAQxL6uJrQ'; // Set your mapbox token here

function App() {
  const [viewState, setViewState] = useState({
    latitude: 37.8,
    longitude: -122.4,
    zoom: 14
  });

  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(true);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      position => {
        setViewState({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          zoom: 14
        });
      },
      () => {
        console.error('Unable to retrieve your location');
      }
    );
  }, []);

  const toggleSidebar = () => {
    setIsSidebarCollapsed(!isSidebarCollapsed);
  };

  const closeSidebar = () => {
    if (!isSidebarCollapsed) {
      setIsSidebarCollapsed(true);
    }
  };

  return (
    <div style={{ position: 'relative', height: '100vh' }}>
      <Sidebar
        aria-label="Sidebar with multi-level dropdown example"
        style={{
          position: 'absolute',
          top: '5vh',
          left: isSidebarCollapsed ? '-30vw' : '0',
          height: '90vh',
          width: '30vw',
          whiteSpaceCollapse: 'none',
          overflow: 'hidden',
          transition: 'left 0.4s',
          margin: '0', // Remove margins for better positioning
          background: 'white', // Ensure background is white for better visibility
          boxShadow: '2px 2px 10px rgba(0, 0, 0, 0.3)', // Add shadow for a floating effect
          borderRadius: '10px', // Rounded corners for aesthetics
          zIndex: 1 // Ensure the sidebar is on top
        }}
      >
        <Sidebar.Items>
          <Sidebar.ItemGroup>
            <Sidebar.Item style={{ fontSize: '20px', fontWeight: 'bold' }}>
              Voyager Craft Coffee
            </Sidebar.Item>
          </Sidebar.ItemGroup>
          <Sidebar.ItemGroup>
            <Sidebar.Item>
              Overall Grind Score: 4.7
            </Sidebar.Item>
            <Sidebar.Collapse label='Score Breakdown'>
              <Sidebar.Item href="#">Coffee: 4.2</Sidebar.Item>
              <Sidebar.Item href="#">Environment: 4.5</Sidebar.Item>
              <Sidebar.Item href="#">People: 4.2</Sidebar.Item>
            </Sidebar.Collapse>
          </Sidebar.ItemGroup>
          <Sidebar.ItemGroup>
            <Sidebar.Item>
              Laptop Friendly: Yes
            </Sidebar.Item>
            <Sidebar.Item>
              Bathroom: Yes
            </Sidebar.Item>
            <Sidebar.Item>
              Wifi: Yes
            </Sidebar.Item>
          </Sidebar.ItemGroup>
          <Sidebar.ItemGroup>
            <Sidebar.Item>
              Hours: 6:00am - 10:00pm
            </Sidebar.Item>
            <Sidebar.Item>
              Address: 20807 Stevens Creek Blvd
            </Sidebar.Item>
          </Sidebar.ItemGroup>
        </Sidebar.Items>
      </Sidebar>
      <Map
        {...viewState}
        onMove={evt => setViewState(evt.viewState)}
        onClick={closeSidebar}
        style={{ width: '100vw', height: '100vh' }}
        mapStyle="mapbox://styles/mapbox/streets-v9"
        mapboxAccessToken={MAPBOX_TOKEN}
      >
        <GeolocateControl />
        <NavigationControl />
        <Marker
          longitude={-122.03832035506004}
          latitude={37.32316276559068}
          color="red"
          onClick={(event) => {
            event.originalEvent.stopPropagation(); // Prevent triggering the map's onClick event
            toggleSidebar();
          }}
        />
      </Map>
    </div>
  );
}

export default App;
