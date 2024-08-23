import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ClassEntry from './components/ClassEntry'
import CreateInvoice from './components/CreateInvoice'
import ListInvoices from './components/ListInvoice'
import InvoiceDetail from './components/InvoiceDetail'
import CreateTeacher from './components/CreateTeacher'
import CreateService from './components/CreateService'
import Nav from './components/Nav'

function App() {

  return (
    <>
      <BrowserRouter>
        <Nav />
        <div>
            <Routes>
              <Route path='/' element={<ClassEntry />} />
              <Route path='/createinvoice' element={< CreateInvoice />} />
              <Route path='/listinvoice' element={< ListInvoices />} />
              <Route path='/invoicedetail/:id' element={<InvoiceDetail />} />
              <Route path='/createteacher' element={<CreateTeacher />} />
              <Route path='/createservice' element={<CreateService />} />
            </Routes>
        </div>
      </BrowserRouter>
    </>
  )
}

export default App
