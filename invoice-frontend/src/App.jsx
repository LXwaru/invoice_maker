import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ClassEntry from './components/ClassEntry'
import CreateInvoice from './components/CreateInvoice'
import ListInvoices from './components/ListInvoice'
import InvoiceDetail from './components/InvoiceDetail'
import CreateTeacher from './components/CreateTeacher'
import Nav from './components/Nav'

function App() {

  return (
    <>
      <BrowserRouter>
        <Nav />
        <h1>General Invoicing Application</h1>
        <div>
            <Routes>
              <Route path='/' element={<ClassEntry />} />
              <Route path='/createinvoice' element={< CreateInvoice />} />
              <Route path='/listinvoice' element={< ListInvoices />} />
              <Route path='/invoicedetail/:id' element={<InvoiceDetail />} />
              <Route path='/createteacher' element={<CreateTeacher />} />
            </Routes>
        </div>
      </BrowserRouter>
    </>
  )
}

export default App
