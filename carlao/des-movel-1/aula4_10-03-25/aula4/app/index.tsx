import { Text, View, Image } from "react-native";
import { TextInput } from "react-native-gesture-handler";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}>
        
      <Text>Hello, World</Text>
      <Image source={require('../img/praia.png')} style={{ width: 200, height: 200 }}></Image>
    </View>
  );
}


//   <Text style={Estilos.titulo}>Login</Text>

// <View style={Estilos.main}>
//   <Text style={Estilos.classeNaoImplementada}>Usuario:</Text>
//   <TextInput/>
//   <Text style={Estilos.classeNaoImplementada}>Senha:</Text>
//   <TextInput/>
// </View>