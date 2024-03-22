import {
    Card,
    CardBody,
    CardHeader,
    Typography,
} from "@material-tailwind/react";
import Chart from "react-apexcharts";


const chartConfig = {
type: "pie",
width: 280,
height: 280,
series: [44, 55, 13, 43, 22],
options: {
    chart: {
    toolbar: {
        show: false,
    },
    },
    title: {
    show: "",
    },
    dataLabels: {
    enabled: false,
    },
    colors: ["#020617", "#ff8f00", "#00897b", "#1e88e5", "#d81b60"],
    legend: {
    show: false,
    },
},
};

export default function Audience() {
    return (
        <div className="flex flex-grow gap-x-5 w-screen h-screen bg-base-300 shadow-xl p-10">
            <div className="card basis-1/3 bg-base-100 shadow-xl">
            <figure className="px-10 pt-10">
                <Chart {...chartConfig} />
            </figure>
            <div className="card-body items-center text-center">
                <h2 className="card-title">Countries</h2>
                <p>Breakdown of your audience, country-wise</p>
                <div className="card-actions">
                </div>
            </div>
            </div>
            <div className="card basis-1/3 bg-base-100 shadow-xl">
            <div className="card-body items-center text-center">
            <div className="overflow-x-auto">
                <h1 className="text-xl font-bold">Trending Topics for your Account</h1>
                <table className="table text-lg">
                    {/* head */}
                    <thead>
                    <tr>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    {/* row 1 */}
                    <tr>
                        <th>#1</th>
                        <td>Cy Ganderton</td>
                    </tr>
                    {/* row 2 */}
                    <tr className="hover">
                        <th>#2</th>
                        <td>Hart Hagerty</td>
                    </tr>
                    {/* row 3 */}
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    </tbody>
                </table>
                </div>
            </div>
            </div>
            <div className="card basis-1/3 bg-base-100 shadow-xl">
            <figure className="px-10 pt-10">
                <Chart {...chartConfig} />
            </figure>
            <div className="card-body items-center text-center">
                <h2 className="card-title">Age Group</h2>
                <p>Breakdown of your audience, based on age group</p>
                <div className="card-actions">
                </div>
            </div>
            </div>
        </div>
    )
}