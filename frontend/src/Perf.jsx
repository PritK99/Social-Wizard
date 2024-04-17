import Chart from "react-apexcharts";
 
const chartConfig = {
  type: "line",
  height: 500,
  series: [
    {
      name: "Likes",
      data: [50, 40, 300, 320, 500, 350, 200, 100, 89],
    },
    {
        name: "Comments",
        data: [500, 350, 200, 230, 500, 50, 40, 300, 320],
    },  
  ],
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
    stroke: {
      lineCap: "round",
      curve: "smooth",
    },
    markers: {
      size: 0,
    },
    xaxis: {
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
      labels: {
        style: {
          colors: "#777777",
          fontSize: "12px",
          fontFamily: "inherit",
          fontWeight: 400,
        },
      },
      categories: [
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
    },
    yaxis: {
      labels: {
        style: {
          colors: "#777777",
          fontSize: "12px",
          fontFamily: "inherit",
          fontWeight: 400,
        },
      },
    },
    grid: {
      show: true,
      borderColor: "#777777",
      strokeDashArray: 5,
      xaxis: {
        lines: {
          show: true,
        },
      },
      padding: {
        top: 5,
        right: 20,
      },
    },
    fill: {
      opacity: 0.8,
    },
    tooltip: {
      theme: "dark",
    },
    legend: { // Add the legend configuration
        labels: {
            colors: '#777777' // set legend text color to black
        }
    }
  },
};
 
export default function Perf() {
    return(
        <div className="flex flex-row max-w-screen h-screen bg-base-300 shadow-xl p-4 gap-x-5">
            <div className="card bg-base-200 basis-2/3">
                <Chart {...chartConfig}  className="h-full"/>
            </div>

            <div className="stats stats-vertical shadow basis-1/3">
            <div className="stat">
                <div className="stat-title">Impressions</div>
                <div className="stat-value">31K</div>
                <div className="stat-desc">Jan 1st - Feb 1st</div>
            </div>
            
            <div className="stat">
                <div className="stat-title">New Followers</div>
                <div className="stat-value">420</div>
                <div className="stat-desc">↗︎ 40 (22%)</div>
            </div>
            
            <div className="stat">
                <div className="stat-title">New views</div>
                <div className="stat-value">1,200</div>
                <div className="stat-desc">↘︎ 90 (14%)</div>
            </div>
            
            </div>
        </div>
    )
}