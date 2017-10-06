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
            { "data": "mac_addresses" }

        ]
    } );

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
            { "data": "vlans"}

        ]
    } );

// auto refresh the datatable
setInterval( function () {
    discovery.ajax.reload();
}, 10000 );

setInterval( function () {
    requests.ajax.reload();
}, 10000 );
