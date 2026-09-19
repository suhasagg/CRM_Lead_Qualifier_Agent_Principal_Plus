FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /src
COPY pom.xml .
COPY src src
RUN mvn -q -DskipTests package
FROM eclipse-temurin:21-jre
COPY --from=build /src/target/crm-service-1.0.0.jar /app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
