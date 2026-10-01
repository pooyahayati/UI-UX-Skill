import React from "react";
import {View,TextInput,Text,Pressable} from "react-native";
export default function App(){
  // intentionally requests permission at startup and has one generic upload state
  const [uploading,setUploading]=React.useState(false);
  return <View style={{padding:12,backgroundColor:"#fff"}}>
    <Text>Work Order WO-938 / سفارش</Text>
    <TextInput style={{height:34,borderWidth:1}} placeholder="Notes"/>
    <Pressable onLongPress={()=>{/* delete */}}><Text>Photo</Text></Pressable>
    <Pressable onPress={()=>setUploading(true)}><Text>{uploading?"Uploading...":"Upload"}</Text></Pressable>
  </View>
}