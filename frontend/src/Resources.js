function Resource({HW, availability, capacity}) {
  return (
    <div className="bg-amber-500 flex justify-center rounded-xl h-1/3 p-4 shadow-md my-4">
          <div>
            <div className="flex flex-col max-w-xs">
                <p className="text-base font-bold overflow-auto">Hardware Set</p>
                <p className="text-lg">{HW}</p>
            </div>
            <div className="flex flex-col">
                <p className="text-base font-bold">Resources Available</p>
                <p className="text-lg">{availability}</p>
            </div>
            <div className="flex flex-col">
                <p className="text-base font-bold">Total Capacity</p>
                <p className="text-lg">{capacity}</p>
            </div>
          </div>
    </div>
  );
}



function ResourceTable( {resources} ) {
    return (
      <div>
        <Resource HW={"Computers"} availability={resources.HWSet1Availability} capacity={resources.HWSet1Capacity} />
        <Resource HW={"Servers"} availability={resources.HWSet2Availability} capacity={resources.HWSet2Capacity} />
      </div>
    )
}

export default ResourceTable;