var fadeEffect=[{initialAttr:function(){return{opacity:0}},finalAttr:function(){return{opacity:1}}}];export default{"initial.dataset.thermometer":function(){var a=this,b=a.config;return{"plot.appearing":function(a){var c=a.attr.path.slice(0);return c[13]=c[15]=b.thmBaseY,[{initialAttr:{opacity:0},finalAttr:{opacity:1},slot:'initial'},{initialAttr:{path:c},finalAttr:{opacity:1},slot:'middle'}]},"plot.updating":null,"text.appearing":function(){return fadeEffect[0].slot='final',fadeEffect},"text.updating":null,"labelGroup.appearing":function(){return fadeEffect[0].slot='final',fadeEffect},"labelGroup.updating":null,"path.appearing":function(){return fadeEffect[0].slot='initial',fadeEffect},"path.updating":null}}};