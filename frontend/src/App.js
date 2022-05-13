import React, { useState, useRef } from "react"
import './App.css'

function App() {
  const [calculations, setCalculations] = useState([]);
  const ipRef = useRef()
  const maskRef = useRef()

  function Calculate(event) {
    const ip = ipRef.current.value
    const mask = maskRef.current.value
    let response = fetch(`http://127.0.0.1:8000/ipcalc/${ip}?mask=${mask}`)
      .then(response => response.json())
      .then(json => {
        console.log(json)
        setCalculations(json)
      })
  }


  return (
    <>
      <div className="App">
        <header className="App-header">
        </header>    
        <body className="App-body">    
          <span>Enter an IP and CIDR subnet mask</span>
          <div className="input-container">
            <input id="ip-input" ref={ipRef} type="text" />
            <input id="mask-input" ref={maskRef} type="text" />
            <button className="btn" onClick={() => Calculate()}>Calculate</button>
          </div>
          <div className="Output">
            {Object.keys(calculations).map((key) => (
              <p key={key}>
                <div>{key}</div>
                <div>{calculations[key]}</div>
              </p>
            ))}
          </div>
        </body>
      </div>
    </>
  )
}

export default App;
