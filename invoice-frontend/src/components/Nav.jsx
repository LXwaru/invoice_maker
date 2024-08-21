import { NavLink } from "react-router-dom"

const Nav = () => {
    return (
        <div className="navbar">
            <NavLink to="/">CLASS SIGN IN</NavLink>
            <NavLink to="/createinvoice">CREATE INVOICE</NavLink>
            <NavLink to="/listinvoice">LIST INVOICES</NavLink>
        </div>
    )
}
export default Nav