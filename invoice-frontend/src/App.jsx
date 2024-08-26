import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import ServiceEntry from './components/ServiceEntry'
import CreateInvoice from './components/CreateInvoice'
import ListInvoices from './components/ListInvoice'
import InvoiceDetail from './components/InvoiceDetail'
import CreateClient from './components/CreateClient'
import CreateService from './components/CreateService'
import DeleteClient from './components/DeleteClient'
import Nav from './components/Nav'
import Footer from './components/Footer'

function App() {

  return (
    <>
      <BrowserRouter>
        <Nav />
        <div>
            <Routes>
              <Route path='/' element={<ServiceEntry />} />
              <Route path='/createinvoice' element={< CreateInvoice />} />
              <Route path='/listinvoice' element={< ListInvoices />} />
              <Route path='/invoicedetail/:id' element={<InvoiceDetail />} />
              <Route path='/createclient' element={<CreateClient />} />
              <Route path='/createservice' element={<CreateService />} />
              <Route path='/deleteclient' element={<DeleteClient />} />
            </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  )
}

export default App
