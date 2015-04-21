from django.http import HttpResponse

def home(request):
     return HttpResponse(
	"""
	<!DOCTYPE html>
	<html lang="es">
	<head>
        	<title>Django on Openshift</title>
	        <meta charset="utf-8"/>
        	<meta name="viewport" content="width=device-width, height=device-height"/>
	        <style>
        	  h2 {
	            font-size: 32px;
        	    text-align : center;
          	  }
          	  h3 {
            	    font-size: 32px;
                    text-align: center;
                  }
		  a {
                    color: blue;
                    text-decoration: none;
                  }
        	</style>
	</head>
	<body>
 	<h2><strong>You just deploy Django on OpenShift.</strong></h2>
 	<h3><a href="/admin">Admin Console</a>
	</body>
	"""
     )

