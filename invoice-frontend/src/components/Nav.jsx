import { NavLink } from "react-router-dom"

const Nav = () => {
    return (
        <>
        <nav className='navbar bg-body-tertiary fixed-top'>
            <div className="container-fluid">
                <NavLink className="navbar-brand" to='/'>Simple Solutions</NavLink>
                <button className="navbar-toggler" type="button" data-bs-toggle='offcanvas' data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className='offcanvas offcanvas-end' tabIndex='-1' id='offcanvasNavbar' aria-labelledby="offcanvasNavbarLabel">
                <div className="offcanvas-header">
                    <h5 className="offcanvas-title" id="offcanvasNavbarLabel">Simple Solutions</h5>
                    <button type="button" className="btn-close" aria-label="Close"></button>
                </div>
                <div className="offcanvas-body">
                    <ul className="navbar-nav justify-content-end flex-grow-1 pe-3" data-bs-dismiss="offcanvas">
                        <li className="nav-item">
                            <NavLink className="nav-link" to="/serviceentry">CLASS SIGN IN</NavLink>
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
                            <NavLink className="nav-link" to='/createemployee'>REGISTER NEW EMPLOYEE</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="nav-link" to='/createservice'>REGISTER NEW SERVICE</NavLink>
                        </li>

                    </ul>
                </div>
                </div>
            </div>
        </nav>
        </>

        // <div className='nav'>
        //     <ul className="nav fixed-top justify-content-center">
        //         <li className="nav-item">
        //             <NavLink className="nav-link" to="/">CLASS SIGN IN</NavLink>
        //         </li>
        //         <li className="nav-item">
        //             <NavLink className="nav-link" to="/createinvoice">CREATE INVOICE</NavLink>      
        //         </li>
        //         <li className="nav-item">
        //             <NavLink className="nav-link" to="/listinvoice">LIST INVOICES</NavLink>
        //         </li>
        //         <li className="nav-item">
        //             <NavLink className="nav-link" to="/createclient">REGISTER NEW CLIENT</NavLink>
        //         </li>
        //         <li className="nav-item">
        //             <NavLink className="nav-link" to='/createservice'>REGISTER NEW SERVICE</NavLink>
        //         </li>
        //     </ul>
        // </div>
    )
}
export default Nav