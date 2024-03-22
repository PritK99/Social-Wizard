import React from "react";

export default function Content() {
    return (
        <div className="flex flex-grow gap-x-10 w-screen h-screen bg-base-300 shadow-xl p-10">
            <div className="card basis-1/3 bg-base-100 shadow-xl">
                <label className="form-control">
                <div className="label">
                    <span className="label-text text-lg">Enter Topic of Post: </span>
                </div>
                <textarea className="textarea text-lg textarea-bordered textarea-info h-20" placeholder="Topic..."></textarea>
                <div className="label">
                    <span className="label-text text-lg pt-20">Enter Description of the Post: </span>
                </div>
                <textarea className="textarea text-lg textarea-bordered textarea-primary h-60" placeholder="Topic..."></textarea>
                </label>
            </div>
            <div className="flex flex-col justify-between">
            <div className="card flex flex-row basis-2/3 gap-x-5 bg-base-100 shadow-xl">
                <div className="basis-1/2">
                    <p className="text-left">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat facilis quaerat aperiam commodi, et eius doloribus unde vitae ipsam excepturi, voluptatum obcaecati nulla iure fugit eveniet eos est voluptatem dolorum!
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Alias soluta quaerat expedita culpa quia aliquam ipsum, temporibus eligendi ea ex officiis excepturi odit harum dolorem debitis fugit non voluptas maxime.
                    </p>
                </div>
                <figure className="basis-1/2">
                    <img src="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg" alt="Shoes" className="rounded-xl" />
                </figure>
            </div>
            <div className="card-actions justify-center">
                <button className="btn btn-primary">Generate</button>
            </div>
            </div>
        </div>
    )
}