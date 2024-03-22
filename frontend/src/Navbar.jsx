export default function Navbar() {
    return(
      <div className="navbar bg-base-100">
      <div className="flex-1">
        <a href='/' className="btn btn-ghost text-xl">Social Wizard</a>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          <li><a href="/audience">Audience Analysis</a></li>
          <li>
            <a href="/content-gen">Content Generation</a>
          </li>
        </ul>
      </div>
    </div>
    )
}