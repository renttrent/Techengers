import Navbar from "./components/Navbar";
import Button from "./components/Button";
import { useState, useEffect } from "react";
import Axios from "axios";
import { API_HOST, API_PORT } from "./config/config";
// Run with npm run start at */Code/frontend path
// localhost:3000 will open automatically in browser

function App() {
  const [data, setData] = useState({
    name: "Se di",
    job: "Pa pune",
  });

  useEffect(() => {
    Axios.get(`${API_HOST}:${API_PORT}`).then((res) => {
      setData(res.data);
    });
  }, []);

  return (
    <div>
      {/* This is a component */}
      <Navbar />
      <p>Hello Soft Eng</p>
      <p>
        Name: {data.name}, Job: {data.job}
      </p>
      {/* Component with props */}
      <Button name="Yes" />

      <Button name="No" />
    </div>
  );
}

export default App;
