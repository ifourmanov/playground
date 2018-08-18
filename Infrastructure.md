High-performance infrastructure should be designed to minimize communication latency and variance of processing times.
Give a broad explanation of the considerations when designing and managing infrastructure to suit low-latency interactions; 
explain what you would deploy and how you would configure it.

Low latency communication requires establishing points of presense (PoP) close to the information provider/subscriber. 
Depending on latency requirements, information provider physical location and other considerations, options to host processing 
infrastructure include physical datacenters located at or nearby information provider, public cloud providers which provide
availability zones close to target locations or other hosting providers.

Assuming there are multiple Information Providers, the challenge is to provide application platform that would work in the 
same way irrespectable of underlying hosting.

Kubernetes might be selected as a platform, since it's open, well documented and can be deployed to a range of 
underlying systems. Microservices architecture framework can be used to ensure ease of development, making changes and 
isolating complexity. Microservices architecture allows for horizontally scalable environments, where processing times can be improved
by adding more nodes to a component of workload. 

Applications themselves would be run in docker containers, making sure that the same code is run in the same
way on developers machine, test environment or production. CI/CD system in place would run builds of packages, run testsuites,
statical analysis, automated security checks including dependency vulnerability analysis, create release artifacts (docker containers)
and push them to target environment up to production, depending on level of assurance that automated tests can give us.

Applications would communicate via RESTful endpoints on versioned APIs to ensure compatibility and stability of the system 
as a whole. Loadbalancers will distribute requests between multiple instances of the same application.

The key to success lies in a robust and powerful monitoring system, looking at key metrics of our platform, including 
latency of core connections, error rates of applications, core business metrics calculated in time and trend analysis. 
Prometheus + Grafana, ELK stack with Kibana and Elasticsearch Mahine Learning features. Resulting curated alerts should be fed
to NOC/Operations/SRE team using instant messaging, text or push notifications or physical office alerts(monitors, dashboards,
sirens). Events can be used to feed actions into configuration system

Based on monitoring events, additional computational nodes (copies of processes) may be launched (or destroyed) to speed up
processing of needed tasks, as long as there is spare capacity on the hosting cluster. 
