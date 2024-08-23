import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ClassEntry from './components/ClassEntry'
import CreateInvoice from './components/CreateInvoice'
import ListInvoices from './components/ListInvoice'
import InvoiceDetail from './components/InvoiceDetail'
import CreateTeacher from './components/CreateTeacher'
import CreateService from './components/CreateService'
import DeleteTeacher from './components/DeleteTeacher'
import Nav from './components/Nav'
import Footer from './components/Footer'

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
              <Route path='/deleteteacher' element={<DeleteTeacher />} />
            </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  )
}

export default App
