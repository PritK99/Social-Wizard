import React from "react";
import { useState } from "react";
import Markdown from 'react-markdown'

export default function Content() {
    const [topic, setTopic] = useState("");
    const [desc, setDesc] = useState("");
    const [res, setRes] = useState({});
    const [showLoader, setShowLoader] = useState(false);

    let handleSubmit = async () => {
        try {
            setShowLoader(true);
            const response = await fetch('http://127.0.0.1:5000/getContent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'title' : topic, 'description': desc}),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze the essay');
            }

            try {
                const contentResults = await response.json();
                console.log(contentResults);

                setRes(contentResults);
                setShowLoader(false);

            } catch (error) {
                console.error('Failed to parse response JSON', error);
            }
        } catch (error) {
            console.error(error);
        }
        console.log(res["analyze"])
    };

    return (
        <div className="flex flex-grow gap-x-5 max-w-screen h-screen bg-base-300 shadow-xl p-5">
            <div className="card basis-1/3 bg-base-100 shadow-xl">
                <label className="form-control">
                <div className="label">
                    <span className="label-text text-lg">Enter Topic of Post: </span>
                </div>
                <textarea required={true} onChange={(e)=>{setTopic(e.target.value)}} className="textarea text-lg textarea-bordered textarea-info h-auto" placeholder="Topic..."></textarea>
                <div className="label">
                    <span className="label-text text-lg pt-10">Enter Description of the Post: </span>
                </div>
                <textarea onChange={(e)=>{setDesc(e.target.value)}} className="textarea text-lg textarea-bordered textarea-primary h-60" placeholder="Topic..."></textarea>
                </label>
            </div>
            <div className="flex flex-col justify-between basis-2/3 gap-y-5">
            <div className="card flex flex-row basis-2/3 gap-x-5 bg-base-100 shadow-xl w-full">
                {showLoader ? <div className="skeleton w-full h-96"></div> : <><div className="basis-1/2">
                    <p className="text-left">
                    <Markdown>{res["text"]}</Markdown>
                    </p>
                </div>
                <figure className="basis-1/2">
                    <img src={res["image_link"]} className="rounded-xl" />
                </figure></>
                }
            </div>
            <div className="card-actions justify-center">
                <button className="btn btn-primary" onClick={handleSubmit}>Generate</button>
            </div>
            </div>
        </div>
    )
};