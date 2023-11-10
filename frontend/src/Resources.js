function Resource({project}) {

    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.user}</td>
            <td><TextField id="filled-basic" label="QTY" variant="filled" value={qty} onChange={(e) => setQty(e.target.value)}/></td>
            <td className="px-5">
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