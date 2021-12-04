
import models_schemas as ms


app=ms.app
ma=ms.ma
db= ms.db

area_schema= ms.AreaSchema()
areas_schema= ms.AreaSchema(many=True)

school_schema= ms.SchoolSchema()
schools_schema= ms.SchoolSchema(many=True)

department_schema= ms.DepartmentSchema()
departments_schema= ms.DepartmentSchema(many=True)

career_schema= ms.CareerSchema()
careers_schema= ms.CareerSchema(many=True)

course_schema= ms.CourseSchema()
courses_schema= ms.CourseSchema(many=True)


student_schema= ms.StudentSchema()
students_schema= ms.StudentSchema(many=True)



############################################################################################
############################################################################################    
                            ######  #####   ######  ######
                            #    #  #    #  #       #    #
                            ######  #####   ####    ######
                            #    #  #   #   #       #    #
                            #    #  #    #  ######  #    #
############################################################################################
############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################

#GET de lista completa de areas
@app.route("/areas", methods=['GET'])
def get_Areas():
    all_areas = ms.Area.query.all()
    return ms.jsonify(departments_schema.dump(all_areas)),200



#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET area en base un id
@app.route("/areas/<id>", methods=['GET'])
def get_Area(id):
    area = ms.Area.query.get(id)
    if not area is None:
        return area_schema.dump(area),200    
    return ms.jsonify({'message': 'area Not found'}),404





############################################################################################
############################################################################################    
                             #####  ######  #   #  ######  ######   #
                            #       #       #   #  #    #  #    #   #
                            ####    #       #####  #    #  #    #   #
                                 #  #       #   #  #    #  #    #   #
                            #####   ######  #   #  ######  ######   ######
############################################################################################
############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################

#GET de lista completa de facultades
@app.route("/areas/schools", methods=['GET'])
def get_Schools():
    all_schools = ms.School.query.all()
    return ms.jsonify(schools_schema.dump(all_schools)),200

#GET facultades en base a id de area 
@app.route("/areas/<id>/schools", methods=['GET'])
def get_Schools_by_Area(id):
    area = ms.Area.query.get(id)
    if not area is None:
        find_schoools = db.session.query(ms.School).filter(ms.School.area_id ==id)
        return ms.jsonify(schools_schema.dump(find_schoools)),200
    
    return ms.jsonify({'message': 'schools Not found'}),404

#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET facultad en base un id
@app.route("/areas/schools/<id>", methods=['GET'])
def get_School(id):
    school = ms.School.query.get(id)
    if not school is None:
        return school_schema.dump(school),200    
    return ms.jsonify({'message': 'school Not found'}),404

#GET facultad en base el area
@app.route("/areas/<area_id>/schools/<sch_id>", methods=['GET'])
def get_School_of_Department(area_id,sch_id):
    area = ms.Area.query.get(area_id)
    schoool= ms.School.query.get(sch_id)
    if not area is None and not schoool is None:
        school_find= db.session.query(ms.School).filter(ms.School.id==sch_id).join(ms.Area).filter(ms.Area.id==area_id)
        return ms.jsonify(schools_schema.dump(school_find)),200
    
    return ms.jsonify({'message': 'school Not found'}),404





############################################################################################
############################################################################################    
                           #####   ######  #####   #######  
                            #   #  #       #    #     #  
                            #   #  ####    #####      #  
                            #   #  #       #          #  
                           #####   ######  #          #
############################################################################################
############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################

#GET de lista completa de departamentos
@app.route("/areas/schools/departments", methods=['GET'])
def get_Departments():
    all_dept = ms.Department.query.all()
    return ms.jsonify(departments_schema.dump(all_dept)),200

#GET departamentos en base a id de facultades 
@app.route("/areas/schools/<id>/departments", methods=['GET'])
def get_Departments_by_School(id):
    school = ms.School.query.get(id)
    if not school is None:
        find_depts = db.session.query(ms.Department).filter(ms.Department.school_id ==id)
        return ms.jsonify(departments_schema.dump(find_depts)),200
    
    return ms.jsonify({'message': 'departments Not found'}),404

#GET departamentos en base a id de area 
@app.route("/areas/<id>/schools/departments", methods=['GET'])
def get_Departments_by_Area(id):
    area = ms.Area.query.get(id)
    if not area is None:
        
        find_dpts = db.session.query(ms.Department).join(ms.School).join(ms.Area).filter(ms.Area.id==id)
        return ms.jsonify(departments_schema.dump(find_dpts)),200
    
    return ms.jsonify({'message': 'departments Not found'}),404

#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET departamento en base un id
@app.route("/areas/schools/departments/<id>", methods=['GET'])
def get_Department(id):
    dept = ms.Department.query.get(id)
    if not dept is None:
        return department_schema.dump(dept),200
    
    return ms.jsonify({'message': 'department Not found'}),404

#GET departamento en base una facultad
@app.route("/areas/schools/<sch_id>/departments/<dpt_id>", methods=['GET'])
def get_Department_of_School(sch_id,dpt_id):
    school= ms.School.query.get(sch_id)
    dept = ms.Department.query.get(dpt_id)
    if not dept is None and not school is None:
        career_find= db.session.query(ms.Department).filter(ms.Department.id==dpt_id).join(ms.School).filter(ms.School.id==sch_id)
        return ms.jsonify(careers_schema.dump(career_find)),200
    
    return ms.jsonify({'message': 'department Not found'}),404

#GET departamento en base un area
@app.route("/areas/<area_id>/schools/departments/<dpt_id>", methods=['GET'])
def get_Department_of_Area(area_id,dpt_id):
    area= ms.Area.query.get(area_id)
    dept = ms.Department.query.get(dpt_id)
    if not dept is None and not area is None:
        career_find= db.session.query(ms.Department).filter(ms.Department.id==dpt_id).join(ms.School).join(ms.Area).filter(ms.Area.id==area_id)
        return ms.jsonify(careers_schema.dump(career_find)),200
    
    return ms.jsonify({'message': 'department Not found'}),404





############################################################################################
############################################################################################
                    ######  ######  #####   ######  ######   #####  
                    #       #    #  #    #  #       #       #       
                    #       ######  #####   ####    ####      ###     
                    #       #    #  #   #   #       #            #          
                    ######  #    #  #    #  ######  ######   ####
############################################################################################
############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################


#GET de lista completa de cursos
@app.route("/areas/schoools/departments/careers", methods=['GET'])
def get_Careers():
    all_career = ms.Career.query.all()
    return ms.jsonify(careers_schema.dump(all_career)),200


#GET titulaciones en base a id de departamento 
@app.route("/areas/schools/departments/<id>/careers", methods=['GET'])
def get_Careers_by_Dept(id):
    dept = ms.Department.query.get(id)
    if not dept is None:
        careers = db.session.query(ms.Career).filter(ms.Career.department_id ==id)
        return ms.jsonify(careers_schema.dump(careers)),200
    
    return ms.jsonify({'message': 'careers Not found'}),404

#GET titulaciones en base a id de facultad 
@app.route("/areas/schools/<id>/departments/careers", methods=['GET'])
def get_Careers_by_School(id):
    school = ms.School.query.get(id)
    if not school is None:
        careers = db.session.query(ms.Career).join(ms.Department).filter(ms.Department.school_id ==id)
        return ms.jsonify(careers_schema.dump(careers)),200
    
    return ms.jsonify({'message': 'careers Not found'}),404

#GET titulaciones en base a id de area 
@app.route("/areas/<id>/schools/departments/careers", methods=['GET'])
def get_Careers_by_Area(id):
    area = ms.Area.query.get(id)
    if not area is None:
        careers = db.session.query(ms.Career).join(ms.Department).join(ms.School).filter(ms.School.area_id ==id)
        return ms.jsonify(careers_schema.dump(careers)),200
    
    return ms.jsonify({'message': 'careers Not found'}),404


#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET titulaciones en base un id
@app.route("/areas/schools/departments/careers/<id>", methods=['GET'])
def get_Career(id):
    career = ms.Career.query.get(id)
    if not career is None:
        return career_schema.dump(career),200
    
    return ms.jsonify({'message': 'career Not found'}),404

#GET titulacion en base un departamento
@app.route("/areas/schools/departments/<dpt_id>/careers/<car_id>", methods=['GET'])
def get_Career_of_Department(dpt_id,car_id):
    dept = ms.Department.query.get(dpt_id)
    career= ms.Career.query.get(car_id)
    if not dept is None and not career is None:
        career_find= db.session.query(ms.Career).filter(ms.Career.id==car_id).join(ms.Department).filter(ms.Department.id==dpt_id)
        return ms.jsonify(careers_schema.dump(career_find)),200
    
    return ms.jsonify({'message': 'career Not found'}),404

#GET titulacion en base una facultad
@app.route("/areas/schools/<sch_id>/departments/careers/<car_id>", methods=['GET'])
def get_Career_of_School(sch_id,car_id):
    school = ms.School.query.get(sch_id)
    career= ms.Career.query.get(car_id)
    if not school is None and not career is None:
        career_find= db.session.query(ms.Career).filter(ms.Career.id==car_id).join(ms.Department).filter(ms.Department.school_id==sch_id)
        return ms.jsonify(careers_schema.dump(career_find)),200
    
    return ms.jsonify({'message': 'career Not found'}),404

#GET titulacion en base un area
@app.route("/areas/<area_id>/schools/departments/careers/<car_id>", methods=['GET'])
def get_Career_of_Area(area_id,car_id):
    area = ms.Area.query.get(area_id)
    career= ms.Career.query.get(car_id)
    if not area is None and not career is None:
        career_find= db.session.query(ms.Career).filter(ms.Career.id==car_id).join(ms.Department).join(ms.School).filter(ms.School.area_id==area_id)
        return ms.jsonify(careers_schema.dump(career_find)),200
    
    return ms.jsonify({'message': 'career Not found'}),404



############################################################################################
############################################################################################
                ######  ######  #    #  #####   #####   ######  #####
                #       #    #  #    #  #    #  #       #       #
                #       #    #  #    #  #####    ###    ####     ###
                #       #    #  #    #  #   #       #   #           #
                ######  ######  ######  #    #  ####    ######  ####
############################################################################################
############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################

#GET de lista completa de cursos
@app.route("/areas/schools/departments/careers/courses", methods=['GET'])
def get_Courses():
    all_courses = ms.Course.query.all()
    return ms.jsonify(courses_schema.dump(all_courses)),200

#GET cursos en base a id de titulacion
@app.route("/areas/schools/departments/careers/<car_id>/courses", methods=['GET'])
def get_Courses_by_Career(car_id):
    career = ms.Career.query.get(car_id)
    if not career is None:
        courses = db.session.query(ms.Course).filter(ms.Course.career_id ==car_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'courses Not found'}),404

#GET cursos en base a id de departamento
@app.route("/areas/schools/departments/<dpt_id>/careers/courses", methods=['GET'])
def get_Courses_by_Department(dpt_id):
    dept = ms.Department.query.get(dpt_id)
    if not  dept is None:
        courses = db.session.query(ms.Course).join(ms.Career).join(ms.Department).filter(ms.Department.id==dpt_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'courses Not found'}),404

#GET cursos en base a id de facultad
@app.route("/areas/schools/<sch_id>/departments/careers/courses", methods=['GET'])
def get_Courses_by_School(sch_id):
    school = ms.School.query.get(sch_id)
    if not  school is None:
        courses = db.session.query(ms.Course).join(ms.Career).join(ms.Department).filter(ms.Department.school_id==sch_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'courses Not found'}),404

#GET cursos en base a id de area
@app.route("/areas/<area_id>/schools/departments/careers/courses", methods=['GET'])
def get_Courses_by_Area(area_id):
    area = ms.Area.query.get(area_id)
    if not  area is None:
        courses = db.session.query(ms.Course).join(ms.Career).join(ms.Department).join(ms.School).filter(ms.School.area_id==area_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'courses Not found'}),404

#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET curso en base un id
@app.route("/areas/schools/departments/careers/courses/<id>", methods=['GET'])
def get_Course(id):
    course = ms.Course.query.get(id)
    if not course is None:
        return course_schema.dump(course),200
    
    return ms.jsonify({'message': 'course Not found'}),404

#GET curso en base un titulacion
@app.route("/areas/schools/departments/careers/<car_id>/courses/<crs_id>", methods=['GET'])
def get_Course_of_Career(car_id,crs_id):
    career= ms.Career.query.get(car_id)
    course = ms.Course.query.get(crs_id)
    if not course is None and not career is None:
        course_find= db.session.query(ms.Course).filter(ms.Course.id==crs_id).join(ms.Career).filter(ms.Career.id==car_id)
        return ms.jsonify(courses_schema.dump(course_find)),200
    
    return ms.jsonify({'message': 'course Not found'}),404

#GET curso en base a una titulacion y departamento especifico
@app.route("/areas/schools/departments/<dept_id>/careers/courses/<crs_id>", methods=['GET'])
def get_Course_of_Dept(dept_id,crs_id):
    dept = ms.Department.query.get(dept_id) 
    course = ms.Course.query.get(crs_id)
    if not dept is None and not course is None:
        courses = db.session.query(ms.Course).filter(ms.Course.id==crs_id).join(ms.Career).filter(ms.Career.department_id==dept_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'course Not found'}),404

#GET curso en base a una titulacion y departamento especifico
@app.route("/areas/schools/<sch_id>/departments/careers/courses/<crs_id>", methods=['GET'])
def get_Course_of_School(sch_id,crs_id):
    school = ms.School.query.get(sch_id) 
    course = ms.Course.query.get(crs_id)
    if not school is None and not course is None:
        courses = db.session.query(ms.Course).filter(ms.Course.id==crs_id).join(ms.Career).join(ms.Department).filter(ms.Department.school_id==sch_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'course Not found'}),404

#GET curso en base a una titulacion y departamento especifico
@app.route("/areas/<area_id>/schools/departments/careers/courses/<crs_id>", methods=['GET'])
def get_Course_of_Area(area_id,crs_id):
    area = ms.Area.query.get(area_id) 
    course = ms.Course.query.get(crs_id)
    if not area is None and not course is None:
        courses = db.session.query(ms.Course).filter(ms.Course.id==crs_id).join(
            ms.Career).join(ms.Department).join(ms.School).filter(ms.School.area_id==area_id)
        return ms.jsonify(courses_schema.dump(courses)),200
    
    return ms.jsonify({'message': 'course Not found'}),404





############################################################################################
############################################################################################
          #####   #######   #   #   ######    ######   #    #   #######   #####
          #          #      #   #     #   #   #        # #  #      #      #
           ###       #      #   #     #   #   ###      #  # #      #       ###
              #      #      #   #     #   #   #        #   ##      #          #
          ####       #      #####   ######    ######   #    #      #      ####
#############################################################################################
#############################################################################################

#############################################################################################
#                                       GET LISTAS                                          #
#############################################################################################

#GET de lista completa de estudiantes
@app.route("/areas/schools/departments/careers/courses/students", methods=['GET'])
def get_Students():
    all_students = ms.Student.query.all()
    return ms.jsonify(students_schema.dump(all_students)),200

#GET estudiantes en base a un curso 
@app.route("/areas/schools/departments/careers/courses/<id>/students", methods=['GET'])
def get_Students_by_Course(id):
    
    course = ms.Course.query.get(id)
    if not course is None:
        students = db.session.query(ms.Student).join(ms.Course).filter(ms.Course.id==id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiantes en base a una titulacion
@app.route("/areas/schools/departments/careers/<id>/courses/students", methods=['GET'])
def get_Students_by_Career(id):
    career = ms.Career.query.get(id)
    if not career is None:
        students = db.session.query(ms.Student).join(ms.Course).filter(ms.Course.career_id==id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiantes en base a un departamento
@app.route("/areas/schools/departments/<id>/careers/courses/students", methods=['GET'])
def get_Students_by_Dept(id):
    dept = ms.Department.query.get(id)
    if not dept is None:
        students = db.session.query(ms.Student).join(ms.Course).join(ms.Career).filter(ms.Career.department_id==id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiantes en base a una facultad
@app.route("/areas/schools/<id>/departments/careers/courses/students", methods=['GET'])
def get_Students_by_School(id):
    school = ms.School.query.get(id)
    if not school is None:
        students = db.session.query(ms.Student).join(ms.Course).join(ms.Career).join(ms.Department).filter(ms.Department.school_id==id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiantes en base a un area
@app.route("/areas/<id>/schools/departments/careers/courses/students", methods=['GET'])
def get_Students_by_Area(id):
    area = ms.Area.query.get(id)
    if not area is None:
        students = db.session.query(ms.Student).join(ms.Course).join(ms.Career).join(ms.Department).join(ms.School).filter(ms.School.area_id==id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#############################################################################################
#                                       GET ESPECIFICO                                      #
#############################################################################################

#GET estudiante en base a su id
@app.route("/areas/schools/departments/careers/courses/students/<id>", methods=['GET'])
def get_Student(id):
    student = ms.Student.query.get(id)
    if not student is None:
        return student_schema.dump(student),200
    
    return ms.jsonify({'message': 'student Not found'}),404

#GET estudiante en base a un curso especifico
@app.route("/areas/schools/departments/careers/courses/<crs_id>/students/<std_id>", methods=['GET'])
def get_Student_of_Course(crs_id,std_id):
    
    course = ms.Course.query.get(crs_id)
    student= ms.Student.query.get(std_id)
    if not course is None and not student is None:
        students = db.session.query(ms.Student).filter(ms.Student.id==std_id).join(ms.Course).filter(ms.Course.id==crs_id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'student Not found'}),404

#GET estudiante en base a un curso y titulacion especifica
@app.route("/areas/schools/departments/careers/<tit_id>/courses/<crs_id>/students/<std_id>", methods=['GET'])
def get_Student_of_Course_and_Career(tit_id,crs_id,std_id):
    career = ms.Career.query.get(tit_id)
    course = ms.Course.query.get(crs_id)
    student= ms.Student.query.get(std_id)
    if not career is None and not course is None and not student is None:
        students = db.session.query(ms.Student).filter(ms.Student.id==std_id).join(ms.Course).filter(ms.Course.id==crs_id).join(
            ms.Career).filter(ms.Career.id==tit_id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiante en base a un curso,titulacion  y departamento especifico
@app.route("/areas/schools/departments/<dept_id>/careers/<tit_id>/courses/<crs_id>/students/<std_id>", methods=['GET'])
def get_Student_of_Course_Career_and_Dept(dept_id,tit_id,crs_id,std_id):
    dept = ms.Department.query.get(dept_id)
    career = ms.Career.query.get(tit_id)
    course = ms.Course.query.get(crs_id)
    student= ms.Student.query.get(std_id)
    if not dept is None and not career is None and not course is None and not student is None:
        students = db.session.query(ms.Student).filter(ms.Student.id==std_id).join(ms.Course).filter(ms.Course.id==crs_id).join(
            ms.Career).filter(ms.Career.id==tit_id).join(ms.Department).filter(ms.Department.id==dept_id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiante en base a un curso,titulacion, departamento y facultad especifica
@app.route("/areas/schools/<sch_id>/departments/<dept_id>/careers/<tit_id>/courses/<crs_id>/students/<std_id>", methods=['GET'])
def get_Student_of_Course_Career_Dept_and_School(sch_id, dept_id,tit_id,crs_id,std_id):
    school = ms.School.query.get(sch_id)
    dept = ms.Department.query.get(dept_id)
    career = ms.Career.query.get(tit_id)
    course = ms.Course.query.get(crs_id)
    student= ms.Student.query.get(std_id)
    if not school is None and not dept is None and not career is None and not course is None and not student is None:
        students = db.session.query(
            ms.Student).filter(ms.Student.id==std_id).join(
                ms.Course).filter(ms.Course.id==crs_id).join(
                    ms.Career).filter(ms.Career.id==tit_id).join(
                        ms.Department).filter(ms.Department.id==dept_id).join(
                            ms.School).filter(ms.School.id==sch_id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404

#GET estudiante en base a un curso,titulacion, departamento y facultad especifica
@app.route("/areas/<area_id>/schools/<sch_id>/departments/<dept_id>/careers/<tit_id>/courses/<crs_id>/students/<std_id>", methods=['GET'])
def get_Student_of_Course_Career_Dept_School_adn_Area(area_id, sch_id, dept_id,tit_id,crs_id,std_id):
    area = ms.Area.query.get(area_id)
    school = ms.School.query.get(sch_id)
    dept = ms.Department.query.get(dept_id)
    career = ms.Career.query.get(tit_id)
    course = ms.Course.query.get(crs_id)
    student= ms.Student.query.get(std_id)
    if not (area, school, dept, career, course, student) is None:
        students = db.session.query(
            ms.Student).filter(ms.Student.id==std_id).join(ms.Course).filter(ms.Course.id==crs_id).join(
                    ms.Career).filter(ms.Career.id==tit_id).join(ms.Department).filter(ms.Department.id==dept_id).join(
                            ms.School).filter(ms.School.id==sch_id).join(ms.Area).filter(ms.Area.id==area_id)
        return ms.jsonify(students_schema.dump(students)),200
    
    return ms.jsonify({'message': 'students Not found'}),404
