import { StyleSheet, Text, View } from 'react-native';
import { useState, useEffect } from 'react';
import { Accelerometer } from 'expo-sensors';
import * as Location from 'expo-location';
// import Geolocation from '@react-native-community/geolocation';

export default function App() {
  const [ location, setLocation ] = useState({coords: {}});

  useEffect(() => {( async () => {
    const { status } = await Location.requestForegroundPermissionsAsync();

    if (status !== 'granted')
      console.log('Permission to access location was denied')
    
    else {
      const locationSubscription = await Location.watchPositionAsync({
            accuracy: Location.Accuracy.Highest,
            timeInterval: 1000,
            distanceInterval: 1,
      }, (location) => {
        setLocation(location);
        console.log('New location update: ' + location.coords.latitude + ', ' + location.coords.longitude);
      })
    } 
    
    return () => locationSubscription.remove();
  })()}, [])

  return (
    <View>
      <Text>FILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLER</Text>
      <Text>FILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLERFILLER</Text>
      <Text>lat: {location.coords.latitude}</Text>
      <Text>lon: {location.coords.longitude}</Text>
    </View>
  ); 
}

// export default function App() {
//   const [ location, setLocation ] = useState();

//   // useEffect(() => {
//   //   (async () => {
//   //     let { status } = await Location.requestForegroundPermissionsAsync();
//   //     if (status !== 'granted') {
//   //       console.log('Permission to access location was denied');
//   //       return;
//   //     }

//   //     let location = await Location.getCurrentPositionAsync({});
//   //     console.log('location is', location)
//   //     setLocation(location);
//   //   })();
//   // }, []);

//   useEffect(() => {
//     setInterval(() => {
//       console.log('re-pinging gps location...')
  
//       return (async () => {
//         let { status } = await Location.requestForegroundPermissionsAsync();
//         if (status !== 'granted') {
//           console.log('Permission to access location was denied');
//           return;
//         }
  
//         let location = await Location.getCurrentPositionAsync({});
//         console.log('location is', location)
//         setLocation(location);
//       })();
//     }, 10000);
//   }, []);

//   // const [data, setData] = useState({
//   //   prev: {
//   //     x: 'xDefault1',
//   //     y: 'yDefault1',
//   //     z: 'zDefault1'
//   //   },
//   //   curr: {
//   //     x: 'xDefault2',
//   //     y: 'yDefault2',
//   //     z: 'zDefault2'  
//   //   }
//   // });

//   // useEffect(() => {
//   //   Accelerometer.addListener((accelerometerData) => {
//   //     setData((data) => {
//   //       const prevData = {...data.curr};

//   //       return {
//   //         prev: prevData,
//   //         curr: accelerometerData
//   //       }
//   //     });
//   //   });
//   // }, []);
    
//   // function isMoving() {
//   //   console.log('isMoving called')

//   //   console.log('prev is', data.prev)
//   //   console.log('curr is', data.curr)

//   //   if (Math.abs(data.curr.x - data.prev.x) > 0.2 || Math.abs(data.curr.y - data.prev.y) > 0.2) {
//   //     console.log('returning true')
//   //     return true;
//   //   }

//   //   else {
//   //     console.log('returning false')
//   //     return false;
//   //   }
//   // }
  
//   return (
//     <View>
//       <Text>Hello </Text>
//       <Text>{location ? "latitude: " + location.coords.latitude : "loading..."}</Text>
//       <Text>{location ? "longitude: " + location.coords.longitude : "loading..."}</Text>
//     </View>
//   // <View>
//   //   <Text>Accelerometer: (in Gs where 1 G = 9.81 m s^-2)</Text>
//   //   <Text>
//   //     x: {data.curr.x} y: {data.curr.y} z: {data.curr.z} isMoving: {isMoving()}
//   //   </Text>
//   //   <Text>isMoving val: {isMoving()}</Text>
//   // </View>
// 	);
// }

// export default function App() {
//   const [ data, setData ] = useState({
//     lon: null,
//     lat: null
//   });

//   useEffect(() => {
//     setInterval(() => {
//       Geolocation.getCurrentPosition((position) => {
//         console.log("position is", position);

//         setData({
//           lon: position.coords.longitude,
//           lat: position.coords.latitude
//         })
//       }, 
//       undefined,
//       { enableHighAccuracy: true })
//     }, 1000)
//   }, [])

//   return (
//     <View>
//       <Text>longitude: {data.lon}</Text>
//       <Text>latitude: {data.lat}</Text>
//     </View>
//   );
// }

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

// export default function App() {
//   // const [data, setData] = useState({
//   //   prev: {
//   //     x: 'xDefault1',
//   //     y: 'yDefault1',
//   //     z: 'zDefault1'
//   //   },
//   //   curr: {
//   //     x: 'xDefault2',
//   //     y: 'yDefault2',
//   //     z: 'zDefault2'  
//   //   }
//   // });

//   const [ movementData, setMovementData ] = useState({
//     xVel: 0,
//     yVel: 0,
//     speed: 0
//   })
 
//   const G = 9.81;

//   useEffect(() => {
//     Accelerometer.setUpdateInterval(1000);
//     Accelerometer.addListener((accelerometerData) => {
//       const { x, y, z } = accelerometerData;
//       // setData((data) => {
//       //   const prevData = {...data.curr};

//       //   return {
//       //     prev: prevData,
//       //     curr: accelerometerData
//       //   }
//       // });
//       setMovementData((data) => {
//         if (x * G > 1 || x * G < -1)
//           console.log("xAcc in m/s^2 is", x * G);

//         if (y * G > 1 || y * G < -1)
//           console.log("yAcc in m/s^2 is", y * G);

//         if (z * G > 1 || z * G < -1)
//           console.log("zAcc in m/s^2 is", z * G);
//         // console.log("data.xVel is", data.xVel);
//         // console.log("data.yVel is", data.yVel);

//         const currXVel = data.xVel + x * G;
//         const currYVel = data.yVel + y * G;
//         const currSpeed = Math.sqrt(Math.pow(currXVel, 2) + Math.pow(currYVel, 2));  // all calculations in m/s

//         // console.log("currXVel is", currXVel)
//         // console.log("currYVel is", currYVel);
//         // console.log("currSpeed is", currSpeed);
        
//         return {
//           xVel: currXVel,
//           yVel: currYVel,
//           speed: currSpeed
//         }
//       });
//     });
//   }, []);

//   return (
//     <View>
//       <Text>xVel: {movementData.xVel}</Text>
//       <Text>yVel: {movementData.yVel}</Text>
//       <Text>speed: {movementData.speed}</Text>
//     </View>
//   );
// }