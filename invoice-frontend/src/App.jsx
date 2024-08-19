import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ClassEntry from './components/ClassEntry'

function App() {

  return (
    <>
    <h1>Class Sign in</h1>
      <BrowserRouter>
          <ClassEntry />
        
      </BrowserRouter>
    </>
  )
}

export default App
