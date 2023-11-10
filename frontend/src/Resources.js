


function Resource({project}) {
    const  [hwUsed, setHwUsed] = useState(0);
    const [qty, setQty] = useState('');
    
    const handleCheckInOut = (qty) => {
        if(qty === '' || qty === 0 || hwUsed + qty < 0 && qty < 0) {
            return;
        }
        setHwUsed(hwUsed + parseInt(qty));
        setQty('');
    };
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.user}</td>
            <td><TextField id="filled-basic" label="QTY" variant="filled" value={qty} onChange={(e) => setQty(e.target.value)}/></td>
            <td className="px-5">
                <Button variant="contained" onClick={() => handleCheckInOut(qty)} >Check in</Button>
                <div/>
                <Button variant="contained" onClick={() => handleCheckInOut(-qty)}>Check out</Button>
            </td>
            <td>HW Used: {hwUsed}</td>
        </tr>
    );
}



function ResourceTable( {resources} ) {
    return (
    <table>
      <tbody>
        {resources.map((resources) => (
          <Resource key={resources.id} project={project} />
        ))}
      </tbody>
    </table>
    )
}

export default Resources;