import React from "react";
import Avatar from "./Avatar";
import Info from "./Info";
function Card(props){
    return <div>
    <h1 className="heading">My Contacts</h1>
    <div className="card">
      <div className="top">
        <h2 className="name">{props.name}</h2>
        <Avatar imgURL={props.imgURL}/>
      </div>
      <div className="bottom">
       <Info info={props.phone} />
       <Info info={props.email} />
       
      </div>
    </div>
  </div>
}


export default Card;