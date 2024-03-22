

import { useState } from 'react'; // Import useState hook to manage state
import Chart from "react-apexcharts";

export default function Audience() {
    const [series1, setSeries1] = useState([]);

    const [series2, setSeries2] = useState([]);

    const [labels1, setLabels1] = useState([]);

    const chartData1 = {
        type: "pie",
        width: 280,
        height: 280,
        series: series1,
        labels: labels1,
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
    }
    const chartData2 = {
        
        series: series2,
        labels : ['0-20', '20-40', '60+'],
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
    }
    

    const handleRunButtonClick = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/getAnalysis', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'userName' : "SRAVJTI" }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze the essay');
            }

            try {
                const analysisResults = await response.json();
                console.log(analysisResults);

                // Update chart series with analysisResults data
                // setChartData1({
                //     ...chartData1,
                //     series: analysisResults.location_frequencies,
                //     labels: analysisResults.top_3_locations
                // });

                // setChartData2({
                //     ...chartData2,
                //     series: analysisResults.age_groups,
                //     labels: ['0-20','20-40','60+']
                // });

                setLabels1(analysisResults.top_3_locations);
                setSeries1(analysisResults.location_frequencies);
                setSeries2(analysisResults.age_groups);

            } catch (error) {
                console.error('Failed to parse response JSON', error);
            }
        } catch (error) {
            console.error(error);
        }
    };

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
                            <button className="btn btn-primary" onClick={handleRunButtonClick}>Submit</button>
                        </div>
                    </label>
                </div>
                <div className="card bg-base-100 basis-1/2 shadow-xl p-5">
                    <figure className="px-5 pt-5">
                        <Chart {...chartData1} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0">Countries</h2>
                        <p>Breakdown of your audience, country-wise</p>
                        <div className="card-actions"></div>
                    </div>
                </div>
            </div>
            <div className="card basis-1/3 bg-base-100 shadow-xl p-0">
                <div className="card-body items-center text-center">
                    <h1 className="text-xl font-bold">Trending Topics</h1>
                    <div className="p-0">
                        <table className="table text-lg">
                            <tbody className="pt-0">
                                {/* Table body */}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div className="basis-1/3 flex flex-col gap-y-5">
                <div className="card bg-base-100 basis-1/2 shadow-xl p-5">
                    <figure className="px-5 pt-5">
                        <Chart {...chartData2} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0">Age Groups</h2>
                        <p>Breakdown of your audience, age-wise</p>
                        <div className="card-actions"></div>
                    </div>
                </div>
                <div className="card bg-zinc-500 basis-1/2 shadow-xl justify-center">
                    <p className="text-lg">Best time to upload: </p>
                    <p className="text-3xl align-middle">10:30pm IST</p>
                </div>
            </div>
        </div>
    );
}















































   
