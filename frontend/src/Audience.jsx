import {
    Card,
    CardBody,
    CardHeader,
    Typography,
} from "@material-tailwind/react";
import Chart from "react-apexcharts";


const chartConfig1 = {
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
    colors: ["#4CAF50","#FFC107" ,"#2196F3" ,"#FF5722" ,"#9C27B0" ],
    legend: {
    show: false,
    },
},
};


const chartConfig2 = {
    type: "pie",
    width: 280,
    height: 280,
    series: [40, 59, 10, 46, 22],
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
        <div className="flex flex-grow gap-x-5 w-screen h-screen bg-base-300 shadow-xl p-4">
            <div className="basis-1/3 flex flex-col gap-y-5">
                <div className="card bg-base-100 basis-1/2 shadow-xl">
                    <label className="form-control text-center">
                    <div className="label">
                        <span className="label-text text-sm">Enter Twitter ID: </span>
                    </div>
                    <div className="flex flex-row gap-x-5">
                        <input type="text" placeholder="example_123" className="input input-bordered w-full max-w-lg" />
                        <button className="btn btn-primary">Submit</button>
                    </div>
                    </label>
                </div>
                <div className="card bg-base-100 basis-1/2 shadow-xl p-5">
                    <figure className="px-5 pt-5">
                        <Chart {...chartConfig1} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0">Countries</h2>
                        <p>Breakdown of your audience, country-wise</p>
                        <div className="card-actions">
                        </div>
                    </div>
                </div>
            </div>
            <div className="card basis-1/3 bg-base-100 shadow-xl p-0">
            <div className="card-body items-center text-center">
            <h1 className="text-xl font-bold">Trending Topics</h1>
            <div className="p-0">
                <table className="table text-lg ">
                    {/* head */}
                    {/* <thead>
                    <tr>
                        <th></th>
                    </tr>
                    </thead> */}
                    <tbody className="pt-0">
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
                    <tr>
                        <th>#4</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    <tr>
                        <th>#3</th>
                        <td>Brice Swyre</td>
                    </tr>
                    
                    </tbody>
                </table>
                </div>
            </div>
            </div>
            <div className="basis-1/3 flex flex-col gap-y-5">
                <div className="card bg-base-100 basis-1/2 shadow-xl p-5">
                    <figure className="px-5 pt-5">
                        <Chart {...chartConfig2} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0">Countries</h2>
                        <p>Breakdown of your audience, country-wise</p>
                        <div className="card-actions">
                        </div>
                    </div>
                </div>
                <div className="card bg-zinc-500 basis-1/2 shadow-xl justify-center">
                    <p className="text-lg">Best time to upload: </p>
                    <p className="text-3xl align-middle">10:30pm IST</p>
                </div>
            </div>
        </div>
    )
}