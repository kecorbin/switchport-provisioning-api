/**
 * Created by kecorbin on 10/6/17.
 */


var discovery = $('#discovery-table').DataTable( {
    "ajax": {
            "type" : "GET",
            "url" : "/api/discovery/link",
            "dataSrc": function ( json ) {
                return json;
            }
            },
    "columns": [
                    { "data": "id" },
                    { "data": "switch" },
                    { "data": "interface" },
                    { "data": "mac_addresses" },
                    { "data": "id",
                        "render": function (data, type, row, meta) {
                            discovery_id = row.id
                       return ' <button onclick="deleteDiscovery(discovery_id)" class="btn btn--icon btn--small btn--negative"><span class="icon-trash"></span></button>'
                        }
                    }
                ]
    }
);


var requests = $('#provisioning-table').DataTable( {
    "ajax": {
            "type" : "GET",
            "url" : "/api/provisioning/port",
            "dataSrc": function ( json ) {
                return json;
            }
            },
    "columns": [
            { "data": "id" },
            { "data": "requestor" },
            { "data": "switch" },
            { "data": "interface" },
            { "data": "vlans"},
            { "data": "id",
                "render": function (data, type, row, meta) {
                    provisioning_id = row.id
               return '<button onclick="deleteRequest(provisioning_id)" class="btn btn--icon btn--small btn--negative"><span class="icon-trash"></span></button>'
                }
            }


        ]
    } );

function deleteDiscovery(id) {
    $.ajax({
        url: '/api/discovery/link/' + id,
        method: 'DELETE'
    })
    discovery.ajax.reload();
}

function deleteRequest(id) {
    $.ajax({
        url: '/api/provisioning/port/' + id,
        method: 'DELETE'
    })
    requests.ajax.reload();
}


// auto refresh the datatable
setInterval( function () {
    discovery.ajax.reload();
}, 10000 );

setInterval( function () {
    requests.ajax.reload();
}, 10000 );
