# Plan Rector de Integración Global del Ecosistema LEXBOT
**Versión:** 1.0  
**Fecha:** 2026-10-14  
**Estado:** documentado en rama aislada; ejecución progresiva pendiente de evidencia por hito.  
**Principio rector:** integrar sin desintegrar; demostrar y no prometer.

## 1. Visión y objetivo
Construir un ecosistema coordinado en el que repositorios, capacidades, automatizaciones y agentes colaboren para producir resultados verificables. Cada componente conserva su responsabilidad. Una capacidad no se considera operativa solo por figurar en un inventario.

El sistema debe recibir un objetivo autorizado, descomponerlo en tareas, seleccionar capacidades existentes, ejecutar únicamente acciones permitidas, verificar las salidas, registrar trazabilidad y conservar evidencia reutilizable. La autonomía se limita a políticas y permisos configurados; no significa permiso ilimitado.

## 2. Principios no negociables
1. Evidence-First: ningún componente se declara operativo sin evidencia reproducible.
2. Reutilizar antes de construir: revisar capacidades y herramientas existentes antes de crear duplicados.
3. Human Governance: acciones jurídicas sustantivas, irreversibles, externas o de alto impacto requieren autorización humana cuando la política lo determine.
4. Aislamiento por defecto: auditorías, prototipos y pilotos se ejecutan en ramas y entornos aislados.
5. No cambiar productos estables, fusionar, desplegar ni publicar sin autorización específica.
6. Trazabilidad: vincular objetivo, actor/agente, capacidad, entradas, permisos, resultado, commit, pruebas y evidencia.
7. Fallos visibles: error, incertidumbre o falta de evidencia producen estado explícito, nunca éxito supuesto.
8. Validar la estructura de una fuente jurídica no demuestra autenticidad, vigencia ni aplicabilidad.

## 3. Las cinco capas

### Capa 1 — Misión y límites de cada repositorio
Definir por repositorio: misión, responsable funcional, estado, interfaz, dependencias, permisos, pruebas, riesgos, coste de mantenimiento y siguiente resultado verificable.

Entregables: mapa de repositorios; fichas versionadas; clasificación activo, experimental, archivado o desconocido; dependencias y zonas protegidas.

Aceptación: cada repositorio accesible del alcance tiene misión y estado sustentados por evidencia o una excepción explícita. Registrar el SHA inspeccionado; no asumir que código y despliegue coinciden.

### Capa 2 — Registro y consumo de capacidades
Usar ECO-CAPABILITIES como inventario canónico existente de 120 capacidades, sin rehacerlo ni asumir que todas están implementadas o certificadas.

Por capacidad: confirmar ID y clasificación X/Y/Z/W/R; localizar implementación; definir entrada/salida; revisar permisos y dependencias; ejecutar prueba aislada; registrar evidencia, límites y consumidores autorizados.

Aceptación: solo marcar VERIFIED_FOR_USE con prueba reproducible, resultado persistente, límites documentados y permisos revisados. El catálogo por sí solo no satisface el criterio.

### Capa 3 — Integraciones y automatizaciones
Identificar las tres integraciones de automatización existentes y sus funciones reales, sin reemplazarlas ni duplicar su responsabilidad.

Inspeccionar disparadores, entradas/salidas, permisos sin exponer secretos, reintentos, efectos externos, idempotencia, registro de errores y mecanismo de apagado. Definir contratos de intercambio y prevenir ciclos o ejecuciones duplicadas.

Aceptación: una integración solo se declara operativa para un flujo cuando existe ejecución identificada, resultado verificable, control de duplicados y evidencia de fallo seguro o recuperación.

### Capa 4 — Coordinación de agentes mediante ECO-BRAIN
Usar Mission Control como capa coordinadora, separando planificación, autorización, ejecución y verificación.

Flujo de referencia:
TASK → MEMORY → CONTEXT → COGNITION → AUTHORIZED TOOL → RESULT → VERIFICATION → TRACE → MEMORY

Cada tarea recibe identificadores estables de misión y trazabilidad. El agente informa qué capacidad propone utilizar, qué permisos necesita y qué resultado espera. Las acciones no autorizadas quedan como propuestas, nunca como ejecutadas.

Entregables: contratos de tarea; política de selección de capacidades; estados explícitos proposed, authorized, running, verified, blocked y failed; límites de reintento y detención.

Aceptación: piloto de extremo a extremo con mission_id y trace_id, evidencia por etapa, fallo seguro y prueba de que una acción propuesta no se presenta como ejecutada.

### Capa 5 — Evidencia, gobierno y control continuo
Conectar ejecuciones con evidencia persistente, pruebas, revisión y estado de liberación.

Cadena obligatoria:
objetivo → automation_id/mission_id → run_id → trace_id → actor → inputs → outputs → commit observado → CI → artifact/evidencia → revisión

Entregables: registro de ejecución; enlaces a logs, pruebas y artefactos; informe de aceptación; revisión humana asociada a un commit exacto; historial de decisiones y excepciones.

Aceptación: un tercero autorizado puede reconstruir qué se ejecutó, sobre qué commit, con qué entradas y permisos, el resultado y la revisión. La ausencia de un eslabón se registra como brecha.

## 4. Repositorios funcionales de referencia
El mapa inicial verificará, no presumirá, estas responsabilidades conocidas:
- ECO-AUTOMATIONS: catálogo y ejecución de automatizaciones.
- ECO-CAPABILITIES: registro de capacidades y evidencia de reutilización.
- ECO-BRAIN: coordinación cognitiva, contexto, herramientas autorizadas y trazabilidad.
- EVIDENCE-CENTER: preservación y consulta de evidencia.
- AUREA-GOVERNANCE: políticas, permisos y decisiones de gobierno.
- VERCELOPS: construcción, despliegue y comprobación operativa.
- LEXBOT-CIVIL y LEXBOT Sintética: productos y pruebas jurídicas, separados de la coordinación.

Estas asignaciones son hipótesis de trabajo basadas en la organización existente; deben confirmarse contra código, configuración y ejecuciones. No implican que los repositorios estén conectados ni que sus módulos estén operativos.

## 5. Hitos verificables

| Hito | Trabajo | Evidencia exigida | Criterio de salida |
|---|---|---|---|
| H0 — Línea base | Fijar referencias, ramas y límites protegidos | commits, ramas, inventarios y exclusiones | base reproducible sin cambios en productos estables |
| H1 — Mapa de repositorios | Revisar repositorios accesibles y asignar misión/estado | fichas, enlaces y SHA inspeccionados | cobertura del alcance y excepciones documentadas |
| H2 — Capacidades | Seleccionar grupo inicial y probar consumo real | pruebas, logs, outputs, CI, límites y consumidores | ninguna capacidad aprobada solo por catálogo |
| H3 — Integraciones | Documentar las tres automatizaciones y sus contratos | IDs de ejecución, entradas/salidas, permisos y fallos probados | intercambio controlado sin duplicación ni efectos no autorizados |
| H4 — Piloto coordinado | Ejecutar flujo completo en entorno aislado | mission_id, trace_id, run_id, commit, CI y artefacto | resultado reproducible y fallo seguro demostrado |
| H5 — Aceptación | Ejecutar pruebas funcionales y de seguridad | matriz, resultados y defectos abiertos | bloqueantes cerrados o decisión documentada |
| H6 — Revisión humana | Revisar evidencia sobre SHA exacto | revisión, fecha, alcance y decisión | decisión humana explícita y trazable |
| H7 — Liberación | Evaluar fusión/despliegue por separado | PR, CI final, permisos, revisión y autorización | liberar solo si todas las condiciones se cumplen |

Crear este documento no completa ningún hito. Cada hito necesita su propia evidencia.

## 6. Métricas
- Cobertura de inventario: repositorios revisados / repositorios accesibles del alcance.
- Capacidades con evidencia: capacidades probadas / capacidades seleccionadas.
- Éxito reproducible: ejecuciones exitosas repetidas / ejecuciones de prueba.
- Trazabilidad completa: ejecuciones con identificadores y artefactos requeridos / ejecuciones auditables.
- Duplicación: flujos con ejecuciones duplicadas / flujos ejecutados.
- Fallos seguros: pruebas negativas bloqueadas correctamente / pruebas negativas ejecutadas.
- Defectos bloqueantes abiertos, por severidad.
- Decisiones humanas pendientes de revisión, permisos, fusión o despliegue.

No se asignan porcentajes objetivo hasta obtener una línea base real o aprobación expresa del equipo.

## 7. Autonomía graduada
- Nivel A — Observación: inventariar, leer, comparar y reportar sin modificar.
- Nivel B — Preparación aislada: crear propuestas, pruebas y documentación en ramas de trabajo.
- Nivel C — Ejecución controlada: ejecutar pruebas y automatizaciones de bajo riesgo dentro de permisos limitados y con trazabilidad.
- Nivel D — Acción externa o sensible: publicación, despliegue, fusión, modificación de productos estables, comunicaciones externas o actos jurídicos sustantivos; requiere autorización específica cuando corresponda.

El paso entre niveles requiere evidencia, permisos mínimos y evaluación de riesgo. La aprobación general del plan no elimina autorizaciones específicas.

## 8. Primer piloto recomendado
Continuar a partir de la prueba de consumo de CAP-002 de ECO-BRAIN, cuyo CI registró seis pruebas aprobadas para el contrato de Mission Control. Esto demuestra ese contrato bajo las condiciones probadas, no la integración completa de las 120 capacidades.

El siguiente piloto debe escoger un flujo pequeño con: objetivo sintético no sensible; capacidad con prueba existente; automatización identificada; coordinación mediante ECO-BRAIN; evidencia registrada; fallo seguro; CI posterior y revisión de resultados. El flujo exacto se seleccionará después de inspeccionar integraciones y permisos reales.

## 9. Exclusiones
- No fusionar ni desplegar automáticamente por este plan.
- No alterar ECO-CONTINUITY-001, ECO-CEL ni ECO-SHIP durante actividades de inspección o recuperación cubiertas por la restricción vigente.
- No probar contra repositorios externos o servicios reales sin autorización y entorno aprobados.
- No exponer secretos en logs.
- No declarar completa TC-001–TC-015 mientras existan pruebas pendientes.
- No tratar el éxito de CI como validación jurídica sustantiva.
- La revisión jurídica humana debe vincularse al commit examinado.

## 10. Estado inicial y siguiente acción
Estado inicial conocido: inventario canónico de 120 capacidades existente; consumo controlado de CAP-002 con CI exitoso; en LEXBOT Sintética, el workflow 38672570968 terminó success sobre el commit 41467801c77d9bdbabf467913416a4ef869be0c7; PR #1 sigue abierto y sin fusionar. La suite TC-001–TC-015 y la revisión jurídica humana siguen pendientes.

Siguiente acción verificable: completar H0 con referencias actuales y límites protegidos; después ejecutar H1 sobre repositorios accesibles sin modificar productos estables. El resultado debe ser una matriz con SHA observado, misión, estado, dependencias, permisos y evidencia, además de un informe de brechas.

Regla de cierre: ninguna fase se marca terminada hasta que el artefacto exista, pueda recuperarse desde el repositorio y la evidencia satisfaga el criterio de salida.
