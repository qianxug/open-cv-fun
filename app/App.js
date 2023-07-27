import { StyleSheet, Text, View } from 'react-native';
import { useState, useEffect } from 'react';
import { Accelerometer } from 'expo-sensors';
import * as Location from 'expo-location';

export default function App() {
  const [ location, setLocation ] = useState();

  // useEffect(() => {
  //   (async () => {
  //     let { status } = await Location.requestForegroundPermissionsAsync();
  //     if (status !== 'granted') {
  //       console.log('Permission to access location was denied');
  //       return;
  //     }

  //     let location = await Location.getCurrentPositionAsync({});
  //     console.log('location is', location)
  //     setLocation(location);
  //   })();
  // }, []);

  useEffect(() => {
    setInterval(() => {
      console.log('re-pinging gps location...')
  
      return (async () => {
        let { status } = await Location.requestForegroundPermissionsAsync();
        if (status !== 'granted') {
          console.log('Permission to access location was denied');
          return;
        }
  
        let location = await Location.getCurrentPositionAsync({});
        console.log('location is', location)
        setLocation(location);
      })();
    }, 10000);
  }, []);

  // const [data, setData] = useState({
  //   prev: {
  //     x: 'xDefault1',
  //     y: 'yDefault1',
  //     z: 'zDefault1'
  //   },
  //   curr: {
  //     x: 'xDefault2',
  //     y: 'yDefault2',
  //     z: 'zDefault2'  
  //   }
  // });

  // useEffect(() => {
  //   Accelerometer.addListener((accelerometerData) => {
  //     setData((data) => {
  //       const prevData = {...data.curr};

  //       return {
  //         prev: prevData,
  //         curr: accelerometerData
  //       }
  //     });
  //   });
  // }, []);
    
  // function isMoving() {
  //   console.log('isMoving called')

  //   console.log('prev is', data.prev)
  //   console.log('curr is', data.curr)

  //   if (Math.abs(data.curr.x - data.prev.x) > 0.2 || Math.abs(data.curr.y - data.prev.y) > 0.2) {
  //     console.log('returning true')
  //     return true;
  //   }

  //   else {
  //     console.log('returning false')
  //     return false;
  //   }
  // }
  
  return (
    <View>
      <Text>Hello </Text>
      <Text>{location ? "latitude: " + location.coords.latitude : "loading..."}</Text>
      <Text>{location ? "longitude: " + location.coords.longitude : "loading..."}</Text>
    </View>
  // <View>
  //   <Text>Accelerometer: (in Gs where 1 G = 9.81 m s^-2)</Text>
  //   <Text>
  //     x: {data.curr.x} y: {data.curr.y} z: {data.curr.z} isMoving: {isMoving()}
  //   </Text>
  //   <Text>isMoving val: {isMoving()}</Text>
  // </View>
	);
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
