#!/bin/bash

rm *.hgt *.shp *.shx *.dbf *.index *.prj *.sql

for X in *.hgt.zip
do
    unzip $X

    gdal_contour -i 10 -snodata 32767 -a height ${X%%.zip} ${X%%.hgt.zip}c10.shp

    shapeindex ${X%%.hgt.zip}c10.shp
    
    if [ ! -e elevation.sql ]; then
        shp2pgsql -p -s 4326 -I ${X%%.hgt.zip}c10.shp elevation > elevation.sql
    fi
    shp2pgsql -a -D -s 4326 -i ${X%%.hgt.zip}c10.shp elevation >> elevation.sql
done

psql -d gis -U gis -f elevation.sql

