function mpld3_load_lib(url, callback) {
    var s = document.createElement('script');
    s.src = url;
    s.async = true;
    s.onreadystatechange = s.onload = callback;
    s.onerror = function() { 
        console.warn("failed to load library " + url);
    };
    document.getElementsByTagName("head")[0].appendChild(s);
}

// Check if mpld3 is already loaded or load it and draw the figure
if (typeof(mpld3) !== "undefined" && mpld3._mpld3IsLoaded) {
    // mpld3 is already loaded: just create the figure
    drawMpld3Figure();
} else if (typeof define === "function" && define.amd) {
    // require.js is available: use it to load d3/mpld3
    require.config({ paths: { d3: "https://d3js.org/d3.v5" } });
    require(["d3"], function(d3) {
        window.d3 = d3;
        mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.5.10.js", function() {
            drawMpld3Figure();
        });
    });
} else {
    // require.js not available: dynamically load d3 & mpld3
    mpld3_load_lib("https://d3js.org/d3.v5.js", function() {
        mpld3_load_lib("https://mpld3.github.io/js/mpld3.v0.5.10.js", function() {
            drawMpld3Figure();
        });
    });
}


function GK_analysis_figure(mpld3) {
                        
    mpld3.draw_figure("fig1", {"width": 640.0, "height": 480.0, "axes": [{"bbox": [0.125, 0.09999999999999998, 0.775, 0.8], "xlim": [80.0, 100.0], "ylim": [80.0, 100.0], "xdomain": [80.0, 100.0], "ydomain": [80.0, 100.0], "xscale": "linear", "yscale": "linear", "axes": [{"position": "bottom", "nticks": 5, "tickvalues": null, "tickformat_formatter": "", "tickformat": null, "scale": "linear", "fontsize": 12.0, "grid": {"gridOn": true, "color": "#000000", "dasharray": "2,2", "alpha": 0.2}, "visible": true}, {"position": "left", "nticks": 5, "tickvalues": null, "tickformat_formatter": "", "tickformat": null, "scale": "linear", "fontsize": 12.0, "grid": {"gridOn": true, "color": "#000000", "dasharray": "2,2", "alpha": 0.2}, "visible": true}], "axesbg": "#FFFFFF", "axesbgalpha": null, "zoomable": true, "id": "el209201337931545232", "lines": [], "paths": [], "markers": [], "texts": [{"text": "xSv %", "position": [0.5, -0.05989583333333333], "coordinates": "axes", "h_anchor": "middle", "v_baseline": "hanging", "rotation": -0.0, "fontsize": 12.0, "color": "#000000", "alpha": 1, "zorder": 3, "id": "el209201337931543072"}, {"text": "Sv %", "position": [-0.07157258064516128, 0.5], "coordinates": "axes", "h_anchor": "middle", "v_baseline": "auto", "rotation": -90.0, "fontsize": 12.0, "color": "#000000", "alpha": 1, "zorder": 3, "id": "el209201337932048912"}], "collections": [{"offsets": "data01", "xindex": 0, "yindex": 1, "paths": [[[[0.0, -0.5], [0.13260155, -0.5], [0.25978993539242673, -0.44731684579412084], [0.3535533905932738, -0.3535533905932738], [0.44731684579412084, -0.25978993539242673], [0.5, -0.13260155], [0.5, 0.0], [0.5, 0.13260155], [0.44731684579412084, 0.25978993539242673], [0.3535533905932738, 0.3535533905932738], [0.25978993539242673, 0.44731684579412084], [0.13260155, 0.5], [0.0, 0.5], [-0.13260155, 0.5], [-0.25978993539242673, 0.44731684579412084], [-0.3535533905932738, 0.3535533905932738], [-0.44731684579412084, 0.25978993539242673], [-0.5, 0.13260155], [-0.5, 0.0], [-0.5, -0.13260155], [-0.44731684579412084, -0.25978993539242673], [-0.3535533905932738, -0.3535533905932738], [-0.25978993539242673, -0.44731684579412084], [-0.13260155, -0.5], [0.0, -0.5]], ["M", "C", "C", "C", "C", "C", "C", "C", "C", "Z"]]], "pathtransforms": [[4.969039949999533, 0.0, 0.0, 4.969039949999533, 0.0, 0.0]], "alphas": [null], "edgecolors": ["#000000"], "facecolors": ["#0000FF"], "edgewidths": [1.0], "offsetcoordinates": "data", "pathcoordinates": "display", "zorder": 1, "id": "el209201337930202752"}], "images": [], "sharex": [], "sharey": []}], "data": {"data01": [[86.0, 83.0], [83.0, 85.0], [94.0, 100.0]]}, "id": "el209201337931542160", "plugins": [{"type": "reset"}, {"type": "zoom", "button": true, "enabled": false}, {"type": "boxzoom", "button": true, "enabled": false}, {"type": "tooltip", "id": "el209201337930202752", "labels": ["Alisson", "Caoimhin Kelleher", "Adri\u00e1n"], "hoffset": 0, "voffset": 10, "location": "mouse"}]});
    (mpld3);

    }
