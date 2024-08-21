import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ClassEntry from './components/ClassEntry'
import CreateInvoice from './components/CreateInvoice'
import ListInvoices from './components/ListInvoice'
import Nav from './components/Nav'

function App() {

  return (
    <>
      <BrowserRouter>
        <Nav />
        <h2>General Invoicing Application</h2>
        <div>
            <Routes>
              <Route path='/' element={<ClassEntry />} />
              <Route path='/createinvoice' element={< CreateInvoice />} />
              <Route path='/listinvoice' element={< ListInvoices />} />
            </Routes>
        </div>
      </BrowserRouter>
    </>
  )
}

export default App
