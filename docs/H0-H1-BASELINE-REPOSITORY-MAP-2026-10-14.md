# H0 — Línea base y H1 — Mapeo inicial de repositorios LEXBOT
**Fecha de inspección:** 2026-10-14  
**Estado:** parcial; lectura documental verificada, auditoría completa pendiente.  
**Método:** lectura de README desde GitHub en rama predeterminada. Los SHA indicados corresponden al contenido recuperado por la API de GitHub; no certifican el commit de producción ni el funcionamiento en runtime.

## 1. Resultado ejecutivo
La inspección documental inicial confirma que existen repositorios con misiones complementarias: coordinación (ECO-BRAIN), automatización (ECO-AUTOMATIONS), delivery (VERCELOPS), evidencia (EVIDENCE-CENTER), gobernanza (AUREA-GOVERNANCE) y productos jurídicos (LEXBOT-CIVIL y LEXBOT Sintética).

La documentación también declara límites relevantes: EVIDENCE-CENTER y AUREA-GOVERNANCE se encuentran en etapa de organización y no certificados como centros/sistemas operativos; VERCELOPS se describe como preparación progresiva; LEXBOT Sintética indica que su estructura inicial no equivale a un motor jurídico operativo. Por tanto, no procede declarar el ecosistema integrado ni listo para despliegue a partir de estas lecturas.

## 2. Repositorios revisados

| Repositorio | Misión declarada en README | SHA del README inspeccionado | Resultado documental | Pendiente para verificar operación |
|---|---|---|---|---|
| ECO-BRAIN | Coordinación cognitiva: tarea, memoria, contexto, cognición, herramientas autorizadas, verificación y trazabilidad | d42dbaa8177bb6733d30009115b702ee2064d984 | Misión e interfaz conceptual claras; v0.1 foundation initialized | Demostrar loop completo con MISSION_ID y TRACE_ID; verificar logs, tests e integración real |
| ECO-AUTOMATIONS | Experimentar, verificar, documentar y evolucionar automatizaciones independientes | 1d3d1b3281cad443c1e7e0589c9e0482cee41787 | Estados de ciclo de vida definidos; ECO-HEALTH-001 descrito como piloto de observación | Recuperar ejecución real del piloto, permisos, resultado y prueba de fallo seguro |
| ECO-CAPABILITIES | Registro canónico de capacidades, según contexto del proyecto | No obtenido en esta lectura: README.md devolvió 404 en la rama predeterminada | La existencia del repositorio está confirmada, pero no se pudo verificar README en la ruta consultada | Inspeccionar árbol, nombre real del documento, manifiestos e inventario; no inferir que faltan capacidades |
| VERCELOPS | Delivery: install/build, runtime readiness, smoke, deploy, production verify y evidencia | b0d718f011a23324193f7e201f8221d23750cb66 | Se define como preparación progresiva por familias | Demostrar build/runtime/health/deploy solo en entorno autorizado; recuperar IDs y evidencia |
| EVIDENCE-CENTER | Organizar, verificar, auditar y preservar evidencia | 32341715cd2780ccbb092071a0759f9765a2fb17 | Declara etapa ORGANIZACIÓN y NO CERTIFICADO COMO CENTRO OPERATIVO | Verificar ingestión, persistencia, recuperación, procedencia y auditoría con prueba aislada |
| AUREA-GOVERNANCE | Definir límites de autoridad, aprobación, aislamiento e integración | ebd1a4aedf7f57cfb4c5bdbc07443c6a619d3b9c | Declara etapa ORGANIZACIÓN y NO CERTIFICADO COMO SISTEMA AUTÓNOMO | Probar políticas y approval gates; confirmar que acciones no autorizadas se bloquean |
| LEXBOT-CIVIL | Asistencia jurídica dominicana para litigación civil, comercial y laboral con supervisión humana | ae887e27cc5a8f8b3988f158bbba9afaa82efef5 | Misión y arquitectura funcional descritas; catalogación no equivale a certificación jurídica | Ejecutar suite, comprobar fuentes primarias y vigencia, revisar cobertura y validar experiencia del usuario |
| lexbot-sinterico | Laboratorio de casos jurídicos sintéticos penales dominicanos | fea97a8b2a045106429192aab522169c6577a673 | README separa casos sintéticos de reales y advierte que no hay motor jurídico certificado por el mero hecho de existir estructura | Completar TC-001–TC-015, revisar reglas con fuentes y revisión jurídica humana sobre SHA exacto |

## 3. Límites y zonas protegidas
- No modificar ramas principales ni productos estables durante esta fase de observación.
- No fusionar ni desplegar automáticamente como consecuencia del plan.
- Mantener separadas la documentación, la prueba estructural, la ejecución real y la certificación.
- Mantener la suite TC-001–TC-015 y la revisión jurídica humana como condiciones pendientes para LEXBOT Sintética.
- Respetar las restricciones previas sobre ECO-CONTINUITY-001, ECO-CEL y ECO-SHIP.
- No registrar secretos, tokens ni credenciales en la evidencia.

## 4. Brechas prioritarias
1. **Inventario completo:** recuperar el catálogo íntegro de repositorios accesibles, sus ramas principales, estado de archivo y actividad relevante. Esta tabla es una muestra inicial de repositorios estratégicos, no un censo exhaustivo.
2. **Contratos entre componentes:** documentar interfaces reales entre ECO-BRAIN, ECO-AUTOMATIONS, ECO-CAPABILITIES, AUREA-GOVERNANCE, EVIDENCE-CENTER y VERCELOPS.
3. **Pruebas operativas:** obtener IDs de ejecuciones reales y resultados recuperables; README no demuestra runtime.
4. **Capacidades:** localizar el manifiesto y comprobar capacidad por capacidad solo después de confirmar la fuente canónica.
5. **Experiencia B2B:** definir recorrido de usuario, criterios de aceptación, smoke tests y health checks por producto.
6. **Liberación:** exigir build, pruebas, runtime/health, revisión humana aplicable y autorización específica antes de desplegar.

## 5. Criterio de salida H0/H1
H0 no se cierra hasta registrar el conjunto de repositorios dentro del alcance, ramas principales y restricciones protegidas con evidencia recuperable. H1 no se cierra hasta que cada repositorio accesible tenga una ficha basada en fuente observada, misión, estado, SHA, dependencias, permisos, pruebas, riesgos y siguiente acción verificable.

## 6. Próximo paso recomendado
Completar el inventario de repositorios y localizar el manifiesto real de ECO-CAPABILITIES; luego inspeccionar los workflows y pruebas de los componentes coordinadores. Priorizar un piloto aislado de extremo a extremo antes de ampliar la integración. No ejecutar despliegues productivos en esta etapa.
