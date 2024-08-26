import { NavLink } from "react-router-dom"

const Nav = () => {
    return (
        <div className='nav'>
            <ul className="nav fixed-top justify-content-center">
                <li className="nav-item">
                    <NavLink className="nav-link" to="/">CLASS SIGN IN</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink className="nav-link" to="/createinvoice">CREATE INVOICE</NavLink>      
                </li>
                <li className="nav-item">
                    <NavLink className="nav-link" to="/listinvoice">LIST INVOICES</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink className="nav-link" to="/createclient">REGISTER NEW CLIENT</NavLink>
                </li>
                <li className="nav-item">
                    <NavLink className="nav-link" to='/createservice'>REGISTER NEW SERVICE</NavLink>
                </li>
            </ul>
        </div>
    )
}
export default Nav