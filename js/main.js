function findStronghold() {
	var Xcoord1 = document.getElementById("inputXcoord1").value;
	var Zcoord1 = document.getElementById("inputZcoord1").value;
	var Xcoord2 = document.getElementById("inputXcoord2").value;
	var Zcoord2 = document.getElementById("inputZcoord2").value;
	
	var Xcoord3 = document.getElementById("inputXcoord3").value;
	var Zcoord3 = document.getElementById("inputZcoord3").value;
	var Xcoord4 = document.getElementById("inputXcoord4").value;
	var Zcoord4 = document.getElementById("inputZcoord4").value;

	var Mline1 = (Zcoord1-Zcoord2)/(Xcoord1-Xcoord2);
	var Mline2 = (Zcoord3-Zcoord4)/(Xcoord3-Xcoord4);

	var Bline1 = Zcoord1 - (Mline1 * Xcoord1);
	var Bline2 = Zcoord3 - (Mline2 * Xcoord3);

	var EndX = Math.round( (Bline1 - Bline2) / (Mline2 - Mline1) );
	var EndY = Math.round( (Mline1 * EndX) + Bline1 );
	
	document.getElementById("finalAlert").innerHTML = 
	`<div class="alert alert-success" role="alert">
		The stronghold is likely around <strong>X: ` + EndX + `</strong> and <strong>Y: ` + EndY + `</strong>
	</div>`;

	return false;
}