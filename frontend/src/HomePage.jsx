export default function HomePage() {
    return (
        <div className="card flex flex-col w-screen h-screen shadow-xl image-full p-0">
            <figure><img src="https://i.pinimg.com/originals/81/08/4d/81084d04dbcadec0b75a7d494b253d7d.gif" alt="Shoes" /></figure>
            <div className="card-body">
            <h2 className="text-center text-5xl font-bold p-10">Welcome to Social Wizard</h2>
            <p className=" px-64 mt-72 text-wrap">Struggling to navigate the ever-changing social media landscape? Look no further! 
            Social Wizard is your one-stop shop for crafting winning social media strategies.
            </p>
            <a href="/audience"><button className="btn btn-primary">Get Started</button></a>
            </div>
            
        </div>
    )
}