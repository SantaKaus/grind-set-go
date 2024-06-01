import * as React from 'react';
import { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import Map, { Marker, FullscreenControl, GeolocateControl, NavigationControl, Popup } from 'react-map-gl';
import { Menu, MenuItem, MenuList, MenuButton, Accordion, AccordionItem, AccordionButton, AccordionPanel, AccordionIcon, Button } from "@chakra-ui/react";
import { ScaleFade } from "@chakra-ui/transition";
import 'mapbox-gl/dist/mapbox-gl.css';

const MAPBOX_TOKEN = 'pk.eyJ1Ijoic2FudGFrYXVzIiwiYSI6ImNsd255azRteDE2b2cyam83YmlocmZxYzUifQ.YYF8_g3GceatHAQxL6uJrQ'; // Set your mapbox token here

function App() {
  const [viewState, setViewState] = useState({
    latitude: 37.8,
    longitude: -122.4,
    zoom: 14
  });

  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

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
    setIsSidebarOpen(!isSidebarOpen);
  };

  const closeSidebar = () => {
    setIsSidebarOpen(false);
  };

  return (
    <div className='relative h-screen w-screen'>
      <Map
        {...viewState}
        onMove={evt => setViewState(evt.viewState)}
        onClick={closeSidebar}
        style={{ width: '100vw', height: '100vh' }}
        mapStyle="mapbox://styles/mapbox/standard"
        mapboxAccessToken={MAPBOX_TOKEN}
        doubleClickZoom={true}
        hash={true}
        pitch={55}
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
        >
        </Marker>
      </Map>
      <Menu isOpen={isSidebarOpen}>
          <MenuButton position="absolute"
            top="2.5rem"
            left="1.5rem"></MenuButton>
          <MenuList
            overflow="scroll"
            background="transparent"
            border="none"
            width="30vw"
            maxH="90vh"
          >
            <div className="">
              <ScaleFade initialScale={0.9} in={isSidebarOpen}>
                <Accordion allowToggle width="100%" overflowY="auto" maxH="85vh">
                  <AccordionItem
                    marginTop={0}
                    marginBottom={3}
                    border="none"
                    backgroundColor="rgba(255, 255, 255, 0.75)"
                    borderRadius="20px"
                    color="black"
                  >
                    <AccordionButton
                      borderRadius="30px"
                      size="md"
                      fontWeight={400}
                    >
                      Is it accessible?</AccordionButton>
                    <AccordionPanel p="0" sx={{ borderBottomRadius: "20px" }}>
                        Hey
                    </AccordionPanel>
                  </AccordionItem>
                </Accordion>
              </ScaleFade>
            </div>
          </MenuList>
        </Menu>
    </div>
  );
}

export default App;
