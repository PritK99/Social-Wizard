export default function HomePage() {
    return (
        <div className="card card-side bg-base-100 shadow-xl h-screen max-w-screen rounded-none">
        <figure><img src="https://i.pinimg.com/originals/81/08/4d/81084d04dbcadec0b75a7d494b253d7d.gif" alt="Graph-gif"/></figure>
        <div className="card-body w-0.5">
            <h2 className="text-center text-5xl p-10 font-bold">Welcome to Social Wizard</h2>
            <p className="text-left text-wrap">Struggling to navigate the ever-changing social media landscape? Look no further!
            Social Wizard is your one-stop shop for crafting winning social media strategies.
            </p>
            <a href="/audience"><button className="btn btn-primary">Get Started</button></a>
        </div>
        </div>
    )
}