from __future__ import annotations

import argparse
import re
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


SOURCE_FILES = [
    "AIRA_00E_Canonical_Baseline_Supersedence_and_Release_Train_Register_v1.0.docx",
    "AIRA_01_AVCI_Engineering_Standard_v3.2_Revised.docx",
    "AIRA_01A_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.2_Revised.docx",
    "AIRA_01B_AVCI_Evidence_Audit_Traceability_and_Control_Standard_v1.2_Revised.docx",
    "AIRA_02_Engineering_Blueprint_v5.2_Revised.docx",
    "AIRA_03_Developer_Guide_v4.2_Revised.docx",
    "AIRA_04_Technology_Stack_v9.2_Revised.docx",
    "AIRA_05_AI_Native_Information_Nervous_System_v4.2_Revised.docx",
    "AIRA_06_CLAUDE_MD_Reference_v3.2_Revised.docx",
    "AIRA_07_AI_DevSecOps_Skills_Framework_v3.2_Revised.docx",
    "AIRA_07B_AI_DevSecOps_Team_Transformation_Maturity_and_Progressive_Autonomy_Direction_Standard_v1.2_Revised.docx",
    "AIRA_08_Unit_Testing_Standard_v3.2_Revised.docx",
    "AIRA_08A_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.1_Revised.docx",
    "AIRA_09_Greenfield_Environment_Standard_v3.2_Revised.docx",
    "AIRA_10_MicroFunction_Framework_v3.4_Revised.docx",
    "AIRA_10A_MicroFunction_Design_and_Development_Guide_v2.4_Revised.docx",
    "AIRA_10B_MicroFunction_Framework_Implementation_Standard_v2.3_Revised.docx",
    "AIRA_10C_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.3_Revised.docx",
    "AIRA_10D_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.3_Revised.docx",
    "AIRA_10E_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.3_Revised.docx",
    "AIRA_11_AI_Native_DevSecOps_Standard_v3.3_Revised.docx",
    "AIRA_11A_DevSecOps_Governance_and_Evidence_Control_Standard_v1.3_Revised.docx",
    "AIRA_12A_Dynamic_Frontend_Workspace_UI_Generation_Template_Lifecycle_and_UX_Governance_Standard_v1.2_Revised.docx",
    "AIRA_13_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2_2_Review_and_Revised.docx",
    "AIRA_14_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2_3_Review_and_Revised.docx",
    "AIRA_15_API_and_Integration_Contract_Standard_v2.2_Revised.docx",
    "AIRA_15A_API_Governance_and_Contract_First_Implementation_Guide_v1.2_Revised.docx",
    "AIRA_15A_API_Governance_and_Contract_First_Implementation_Guide_v1_2_Review_and_Revised.docx",
]


SECOND_BATCH_FILES = [
    "AIRA_16_Database_Migration_and_Data_Engineering_Standard_v2.2_Revised.docx",
    "AIRA_16A_Flyway_Initial_Database_Baseline_and_Migration_Governance_Guide_v1.3_Revised.docx",
    "AIRA_16B_Database_Governance_Flyway_Only_Generation_Versioning_and_Migration_Control_Standard_v1.2_Revised.docx",
    "AIRA_17_Security_Identity_Secrets_and_Access_Control_Standard_v2.2_Revised.docx",
    "AIRA_17A_Security_and_Access_Control_Implementation_Guide_v1.2_Revised.docx",
    "AIRA_18_Repository_Bootstrap_and_Golden_Source_Implementation_Guide_v1_2_Review_and_Revised.docx",
    "AIRA_19_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard_v1_3_Review_and_Revised.docx",
    "AIRA_19B_Sprint_0_and_Foundation_Build_Execution_Plan_v1.2_Revised.docx",
    "AIRA_20_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.3_Revised.docx",
    "AIRA_21A_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1_2_Review_and_Revised.docx",
    "AIRA_22A_Prompt_Guardrail_Model_Alias_and_AI_Evaluation_Registry_v1_2_Review_and_Revised.docx",
    "AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx",
    "AIRA_23B_Architecture_Fitness_Function_Catalog_v1.2_Revised.docx",
    "AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx",
    "AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.2_Revised.docx",
    "AIRA_24B_Operations_Incident_AutoHeal_and_Recovery_Runbook_Pack_v1.2_Revised.docx",
    "AIRA_25_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1_3_Review_and_Revised.docx",
    "AIRA_26B_Governed_Knowledge_Automation_Pipeline_Standard_v1_3_Review_and_Revised.docx",
    "AIRA_29_UAT_Business_Readiness_and_Production_Acceptance_Standard_v1.2_Revised.docx",
    "AIRA_30_Release_Deployment_Change_and_CAB_Governance_Standard_v1.4_Revised.docx",
    "AIRA_30A_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.2_Revised.docx",
    "AIRA_31_Production_Operations_SRE_SLA_SLO_and_Service_Management_Standard_v1.2_Revised.docx",
    "AIRA_31A_Observability_Telemetry_and_Evidence_Correlation_Standard_v1.2_Revised.docx",
    "AIRA_32_Business_Process_Role_Permission_and_SBAC_Catalog_v1.2_Revised.docx",
    "AIRA_34_Internal_Audit_Compliance_Evidence_and_Control_Testing_Playbook_v1.2_Revised.docx",
    "AIRA_35_Business_Continuity_Disaster_Recovery_Backup_and_Restore_Validation_Standard_v1.2_Revised.docx",
    "AIRA_36_Business_User_Training_Adoption_and_Change_Management_Plan_v1.2_Revised.docx",
    "AIRA_39A_VS_Code_Codex_System_Builder_Lite_Agent_and_Tool_Setup_Guide_v1.1_Revised.docx",
    "AIRA_39B_Greenfield_AI_DevSecOps_Workstation_Setup_and_System_Builder_Lite_Implementation_Guide_v1.3_Revised.docx",
    "AIRA_39C_Team_Greenfield_AI_DevSecOps_Workstation_and_Governed_Agent_Setup_Playbook_v1.2_Revised.docx",
    "AIRA_40_Login_MicroFunction_Design_Pattern_Working_Reference_v1.2_Revised.docx",
    "AIRA_41_Dynamic_User_Workspace_Framework_v1.2_Revised.docx",
    "AIRA_41_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard_v1.1_Revised.docx",
    "AIRA_41B_System_Builder_and_Governed_AI_Assisted_Change_Generation_Standard_v1.2_Revised.docx",
    "AIRA_42_AI_Governance_and_Runtime_Control_Standard_v1_2_Review_and_Revised.docx",
    "AIRA_42_Composable_Experience_Framework_v1.1_Revised.docx",
    "AIRA_42C_Foundation_PoC_Roadmap_and_Developer_Technology_Immersion_Sequence_Governance_Standard_v1.4_Revised.docx",
    "AIRA_42D_AI_Agent_Identity_Lifecycle_and_Credential_Hygiene_Standard_v1.3_Revised.docx",
    "AIRA_42E_AI_Agent_Runtime_Security_Control_Plane_Standard_v1.3_Revised.docx",
    "AIRA_42F_AI_Agent_Autonomy_Calibration_Identity_Trust_and_Behavioral_Integrity_Standard_v1.3_Revised.docx",
    "AIRA_42G_AI_Agent_Threat_Model_Abuse_Case_and_Attack_Surface_Control_Standard_v1.1_Revised.docx",
    "AIRA_42H_AI_Agent_Tool_MCP_Gateway_and_Action_Authorization_Standard_v1_1_Review_and_Revised.docx",
    "AIRA_42I_AI_Agent_Memory_Context_and_RAG_Integrity_Control_Standard_v1.1_Revised.docx",
    "AIRA_42J_AI_Agent_Red_Team_Evaluation_and_Certification_Gate_Standard_v1.1_Revised.docx",
    "AIRA_42K_AI_Agent_Incident_Response_Kill_Switch_and_Forensics_Runbook_v1.1_Revised.docx",
    "AIRA_42L_AI_Agent_Multi_Agent_Orchestration_and_Delegation_Chain_Control_Standard_v1.1_Revised.docx",
    "AIRA_42M_AI_Agent_Supply_Chain_MCP_Plugin_and_Connector_Governance_Standard_v1.1_Revised.docx",
    "AIRA_42N_AI_Agent_Policy_as_Code_Reference_Pack_and_OPA_SBAC_Rule_Catalog_v1.1_Revised.docx",
    "AIRA_42O_AI_Agent_Runtime_Registry_Schema_and_Evidence_Data_Model_Standard_v1.1_Revised.docx",
    "AIRA_42P_AI_Agent_Registry_API_Flyway_Schema_and_Seeder_Implementation_Guide_v1.1_Revised.docx",
    "AIRA_42Q_AI_Agent_Registry_Admin_Workspace_Review_Workflow_and_Operational_Dashboard_Implementation_Guide_v1.1_Revised.docx",
    "AIRA_42R_AI_Agent_Registry_UAT_Operational_Readiness_and_Production_Acceptance_Standard_v1.1_Revised.docx",
    "AIRA_42S_AI_Agent_Governance_Master_Index_Cross_Reference_Matrix_and_Implementation_Roadmap_v1.1_Revised.docx",
    "AIRA_43_Continuous_Improvement_Auto_Heal_Auto_Learn_and_Auto_Improve_Governance_Standard_v1.2_Revised.docx",
    "AIRA_43_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx",
    "AIRA_43_PoC1A_Login_Security_Intelligence_StepUp_Human_Approval_Execution_Standard_v1.1_Revised.docx",
    "AIRA_43A_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx",
    "AIRA_43C_Login_PoC1_and_PoC1A_Integrated_Control_Pattern_Traceability_and_Acceptance_Matrix_v1.1_Revised.docx",
    "AIRA_43D_Login_PoC1A_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx",
    "AIRA_44_PoC1A_Login_Security_Intelligence_Functionality_Explanation_and_Developer_Guide_v1.1_Revised.docx",
    "AIRA_44A_System_Builder_Implementation_Guide_AI_Agent_Creation_and_Environment_Provisioning_v1.1_Revised.docx",
    "AIRA_44C_Governed_AI_Agent_Inventory_Lifecycle_and_Runtime_Control_Standard_v1.1_Revised.docx",
    "AIRA_45_Mortgage_Experience_Pack_Reference_Implementation_v1.1_Revised.docx",
    "AIRA_45_PoC2_DevSecOps_Pipeline_Evidence_Pack_GitNexus_and_System_Factory_Implementation_Standard_v1.2_Revised.docx",
    "AIRA_45B_PoC2_Controlled_Intake_Scope_RACI_and_Execution_Plan_v1.0_Draft.docx",
    "AIRA_45C_PoC2_Repository_Bootstrap_Branch_Governance_CODEOWNERS_and_PRMR_Template_Pack_v1.0_Draft.docx",
    "AIRA_45D_PoC2_CICD_Pipeline_Stage_Gate_Matrix_and_Toolchain_Verification_Guide_v1.0_Draft.docx",
    "AIRA_45E_PoC2_Evidence_Pack_Manifest_Schema_Folder_Convention_and_Artifact_Retention_Guide_v1.0_Draft.docx",
    "AIRA_45F_PoC2_Security_Scanning_SBOM_DAST_SCA_Secret_and_Container_Scan_Playbook_v1.0_Draft.docx",
    "AIRA_45G_PoC2_GitNexus_Read_Only_Impact_Analysis_and_Derived_Artifact_Generator_Runbook_v1.0_Draft.docx",
    "AIRA_45H_PoC2_Testing_Architecture_Fitness_OPA_SBAC_Policy_and_Regression_Gate_Pack_v1.0_Draft.docx",
    "AIRA_45I_PoC2_Observability_Audit_Redaction_Rollback_and_Safe_Disable_Evidence_Checklist_v1.0_Draft.docx",
    "AIRA_45J_PoC2_Exit_Review_Acceptance_Reusable_Factory_Handoff_and_Improvement_Backlog_Pack_v1.0_Draft.docx",
    "AIRA_46_Dynamic_Workspace_Configuration_Parameter_and_Runtime_Cache_Standard_v1.1_Revised.docx",
    "AIRA_47_Dynamic_Workspace_Developer_Implementation_Guide_v1.1_Revised.docx",
    "AIRA_48_Dynamic_Workspace_Database_and_Flyway_Migration_Specification_v1.1_Revised.docx",
    "AIRA_49_Dynamic_Workspace_API_and_OpenAPI_Contract_Specification_v1.1_Revised.docx",
    "AIRA_50_Dynamic_Workspace_Component_and_Widget_Development_Standard_v1.1_Revised.docx",
    "AIRA_51_Dynamic_Workspace_Security_RBAC_SBAC_ABAC_and_OPA_Policy_Specification_v1.1_Revised.docx",
    "AIRA_52_Dynamic_Workspace_Testing_and_Architecture_Fitness_Function_Standard_v1.1_Revised.docx",
    "AIRA_53_Dynamic_Workspace_Observability_Audit_and_Evidence_Specification_v1.1_Revised.docx",
    "AIRA_54_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.1_Revised.docx",
    "AIRA_55_Dynamic_Workspace_Configuration_Seeder_and_Runtime_Synchronization_Runbook_v1.1_Revised.docx",
    "AIRA_56_Dynamic_Workspace_Frontend_Reference_Implementation_Guide_v1.1_Revised.docx",
    "AIRA_57_Experience_Block_and_Experience_Pack_Authoring_Guide_v1.1_Revised.docx",
    "AIRA_58_Multimodal_AI_Prompt_Artifact_and_Response_Governance_Guide_v1.1_Revised.docx",
    "AIRA_59_Dynamic_Workspace_UX_Accessibility_and_Responsive_Design_Standard_v1.1_Revised.docx",
    "AIRA_60_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.1_Revised.docx",
]


THIRD_BATCH_FILES = [
    "AIRA_61_AI_Assisted_Dynamic_Workspace_and_System_Builder_Standard_v1.2_Revised.docx",
    "AIRA_62_Enterprise_Grade_Industry_Leadership_and_Executable_Governance_Roadmap_Standard_v1.0.docx",
    "AIRA_63_Production_Readiness_Review_and_Operational_Readiness_Review_Standard_v1.0.docx",
    "AIRA_64_Resilience_Lab_Performance_Concurrency_and_Chaos_Testing_Runbook_v1.0.docx",
    "AIRA_65_Policy_as_Code_Implementation_Standard_v1.0.docx",
    "AIRA_66_Evidence_Manifest_Schema_and_Evidence_Pack_Data_Model_v1.0.docx",
    "AIRA_67_API_Event_Schema_Registry_DLQ_and_Replay_Governance_Runbook_v1.0.docx",
    "AIRA_68_Control_Objectives_and_Evidence_Traceability_Matrix_v1.0.docx",
    "AIRA_69_Threat_Modeling_Abuse_Case_and_Secure_Design_Review_Playbook_v1.0.docx",
    "AIRA_70_AI_Evaluation_Red_Team_Guardrail_and_Model_Route_Certification_Standard_v1.0.docx",
    "AIRA_71_Data_Governance_Retention_Privacy_and_Evidence_Classification_Standard_v1.0.docx",
    "AIRA_72_Reference_Implementation_Golden_Paths_Standard_v1.0.docx",
    "AIRA_73_System_Builder_Operating_Manual_and_Maker_Checker_Runbook_v1.0.docx",
    "AIRA_74_Dynamic_Workspace_Production_UX_and_Experience_Pack_Certification_Standard_v1.0.docx",
    "AIRA_75_Dynamic_Workspace_Certification_Checklist_and_Evidence_Template_Pack_v1.0.docx",
    "AIRA_76_Architecture_Fitness_Function_Executable_Gate_Pack_v1.0.docx",
    "AIRA_77_Canonical_Data_Element_Variable_Message_and_Error_Code_Governance_Standard_v1.0.docx",
    "AIRA_78_Canonical_Data_Dictionary_and_Message_Catalog_Physical_Schema_Flyway_Seeder_and_Admin_Workflow_Guide_v1.0.docx",
    "AIRA_79_Initial_Canonical_Data_Dictionary_Domain_Code_and_Message_Error_Seed_Catalog_v1.0.docx",
    "AIRA_80_Data_and_Message_Governance_CICD_Validator_Code_Generation_Template_and_Test_Pack_v1.0.docx",
    "AIRA_81_Message_Localization_Support_Knowledge_Base_and_User_Communication_Governance_Guide_v1.0.docx",
    "AIRA_091_to_094_Compliance_Execution_Guide_and_Register_Adoption_Checklist_v1.0.docx",
    "AIRA-DOC-082_Batch_Scheduled_Long_Running_EOD_Run_Governance_Standard_v1.0.docx",
    "AIRA-DOC-083_Batch_Operations_Restart_Recovery_Reconciliation_Evidence_Runbook_v1.0.docx",
    "AIRA-DOC-084_Reporting_Analytics_Semantic_Layer_BI_Governance_Standard_v1.0.docx",
    "AIRA-DOC-085_Report_Generation_Distribution_Retention_Analytics_Evidence_Template_Pack_v1.0.docx",
    "AIRA-DOC-086_Input_Validation_Data_Integrity_Cross_Layer_Consistency_Governance_Standard_v1.0.docx",
    "AIRA-DOC-087_Frontend_Backend_API_Event_Workflow_Database_Validation_Implementation_Standard_v1.0.docx",
    "AIRA-DOC-088_Validation_Error_Code_Message_Classification_User_Feedback_Governance_Standard_v1.0.docx",
    "AIRA-DOC-089_Validation_Evidence_Testing_Regression_Acceptance_Template_Pack_v1.0.docx",
    "AIRA-DOC-089_Validation_Evidence_Testing_Regression_and_Acceptance_Template_Pack_v1.1_Aligned_Improved.docx",
    "AIRA-DOC-090_Enterprise_Application_Foundation_Coverage_Product_Correctness_Build_Right_Governance_Assessment_v1.0.docx",
    "AIRA-DOC-090A_Enterprise_Application_Control_Coverage_Matrix_Documentation_Action_Plan_v1.0.docx",
    "AIRA-DOC-091_Product_Management_Requirements_Traceability_Value_Realization_Product_Decision_Governance_Standard_v1.0.docx",
    "AIRA-DOC-092_NFR_Performance_Scalability_Capacity_Concurrency_Enterprise_Readiness_Governance_Standard_v1.0.docx",
    "AIRA-DOC-094_Enterprise_Data_Dictionary_Reference_Data_Naming_MDM_Data_Quality_Governance_Standard_v1.0.docx",
    "AIRA-DOC-095_Register_Adoption_Source_Pack_Manifest_Knowledge_Projection_Cross_Reference_Update_Runbook_v1.0.docx",
    "AIRA-DOC-095A_00A_00D_Register_Patch_Set_for_AIRA_DOC_082_to_094_v1.0.docx",
    "AIRA-DOC-095B_Cross_Reference_Revision_Instruction_Pack_for_Existing_AIRA_Standards_v1.0.docx",
    "AIRA-DOC-095C_Knowledge_Projection_OpenKM_Evidence_Path_Source_Pack_Packer_Checklist_v1.0.docx",
]


SOURCE_FILES.extend(SECOND_BATCH_FILES)
SOURCE_FILES.extend(THIRD_BATCH_FILES)


CATEGORIES = {
    "00E": ("00-release-baseline", "Release baseline"),
    "01": ("01-engineering-standards", "Engineering standards"),
    "01A": ("01-engineering-standards", "Engineering standards"),
    "01B": ("01-engineering-standards", "Engineering standards"),
    "02": ("02-engineering-blueprint", "Engineering blueprint"),
    "03": ("03-developer-guide", "Developer guide"),
    "04": ("04-technology-stack", "Technology stack"),
    "05": ("05-ai-native-information-nervous-system", "AI-native information nervous system"),
    "06": ("06-claude-md-reference", "CLAUDE.md reference"),
    "07": ("07-ai-devsecops-skills", "AI DevSecOps skills"),
    "07B": ("07-ai-devsecops-skills", "AI DevSecOps skills"),
    "08": ("08-unit-testing", "Unit testing"),
    "08A": ("08-unit-testing", "Unit testing"),
    "09": ("09-greenfield-environment", "Greenfield environment"),
    "10": ("10-microfunction-framework", "MicroFunction framework"),
    "10A": ("10-microfunction-framework", "MicroFunction framework"),
    "10B": ("10-microfunction-framework", "MicroFunction framework"),
    "10C": ("10-microfunction-framework", "MicroFunction framework"),
    "10D": ("10-microfunction-framework", "MicroFunction framework"),
    "10E": ("10-microfunction-framework", "MicroFunction framework"),
    "11": ("11-ai-native-devsecops", "AI-native DevSecOps"),
    "11A": ("11-ai-native-devsecops", "AI-native DevSecOps"),
    "12A": ("12-frontend-workspace-ui", "Frontend workspace UI"),
    "13": ("13-knowledge-governance", "Knowledge governance"),
    "14": ("14-decision-records", "Decision records"),
    "15": ("15-api-integration-contracts", "API and integration contracts"),
    "15A": ("15-api-integration-contracts", "API and integration contracts"),
    "16": ("16-database-migration-data-engineering", "Database migration and data engineering"),
    "16A": ("16-database-migration-data-engineering", "Database migration and data engineering"),
    "16B": ("16-database-migration-data-engineering", "Database migration and data engineering"),
    "17": ("17-security-identity-access-control", "Security identity and access control"),
    "17A": ("17-security-identity-access-control", "Security identity and access control"),
    "18": ("18-repository-bootstrap-golden-source", "Repository bootstrap and golden source"),
    "19": ("19-gitnexus-foundation-build", "GitNexus and foundation build"),
    "19B": ("19-gitnexus-foundation-build", "GitNexus and foundation build"),
    "20": ("20-cicd-pipeline-evidence-pack", "CI/CD pipeline and evidence pack"),
    "21A": ("21-knowledge-control-plane", "Knowledge control plane"),
    "22A": ("22-prompt-guardrails-login-patterns", "Prompt guardrails and login patterns"),
    "22B": ("22-prompt-guardrails-login-patterns", "Prompt guardrails and login patterns"),
    "23B": ("23-architecture-fitness-login-poc", "Architecture fitness and login PoC"),
    "23C": ("23-architecture-fitness-login-poc", "Architecture fitness and login PoC"),
    "24": ("24-login-runtime-operations", "Login runtime and operations"),
    "24B": ("24-login-runtime-operations", "Login runtime and operations"),
    "25": ("25-knowledge-access-architecture", "Knowledge access architecture"),
    "26B": ("26-knowledge-automation-pipeline", "Knowledge automation pipeline"),
    "29": ("29-uat-production-acceptance", "UAT and production acceptance"),
    "30": ("30-release-change-governance", "Release and change governance"),
    "30A": ("30-release-change-governance", "Release and change governance"),
    "31": ("31-production-operations-observability", "Production operations and observability"),
    "31A": ("31-production-operations-observability", "Production operations and observability"),
    "32": ("32-business-process-access-catalog", "Business process and access catalog"),
    "34": ("34-audit-compliance-evidence", "Audit compliance and evidence"),
    "35": ("35-business-continuity-disaster-recovery", "Business continuity and disaster recovery"),
    "36": ("36-training-adoption-change-management", "Training adoption and change management"),
    "39A": ("39-workstation-system-builder-setup", "Workstation and system builder setup"),
    "39B": ("39-workstation-system-builder-setup", "Workstation and system builder setup"),
    "39C": ("39-workstation-system-builder-setup", "Workstation and system builder setup"),
    "40": ("40-login-microfunction-reference", "Login MicroFunction reference"),
    "41": ("41-dynamic-workspace-system-builder-poc1", "Dynamic workspace, system builder, and PoC1"),
    "41B": ("41-dynamic-workspace-system-builder-poc1", "Dynamic workspace, system builder, and PoC1"),
    "42": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42C": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42D": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42E": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42F": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42G": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42H": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42I": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42J": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42K": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42L": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42M": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42N": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42O": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42P": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42Q": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42R": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "42S": ("42-ai-governance-agent-control", "AI governance and agent control"),
    "43": ("43-continuous-improvement-multimodal-poc1a", "Continuous improvement, multimodal AI, and PoC1A"),
    "43A": ("43-continuous-improvement-multimodal-poc1a", "Continuous improvement, multimodal AI, and PoC1A"),
    "43C": ("43-continuous-improvement-multimodal-poc1a", "Continuous improvement, multimodal AI, and PoC1A"),
    "43D": ("43-continuous-improvement-multimodal-poc1a", "Continuous improvement, multimodal AI, and PoC1A"),
    "44": ("44-system-builder-agent-poc1a", "System builder, AI agents, and PoC1A"),
    "44A": ("44-system-builder-agent-poc1a", "System builder, AI agents, and PoC1A"),
    "44C": ("44-system-builder-agent-poc1a", "System builder, AI agents, and PoC1A"),
    "45": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45B": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45C": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45D": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45E": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45F": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45G": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45H": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45I": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "45J": ("45-poc2-mortgage-experience", "PoC2 and mortgage experience"),
    "46": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "47": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "48": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "49": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "50": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "51": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "52": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "53": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "54": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "55": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "56": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "57": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "58": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "59": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "60": ("46-60-dynamic-workspace", "Dynamic workspace"),
    "61": ("61-ai-assisted-workspace-system-builder", "AI-assisted workspace and system builder"),
    "62": ("62-enterprise-governance-roadmap", "Enterprise governance roadmap"),
    "63": ("63-production-operational-readiness", "Production and operational readiness"),
    "64": ("64-resilience-performance-chaos", "Resilience performance and chaos testing"),
    "65": ("65-policy-as-code", "Policy as code"),
    "66": ("66-evidence-manifest-data-model", "Evidence manifest and data model"),
    "67": ("67-api-event-schema-registry", "API event schema registry"),
    "68": ("68-control-objectives-traceability", "Control objectives and traceability"),
    "69": ("69-threat-modeling-secure-design", "Threat modeling and secure design"),
    "70": ("70-ai-evaluation-red-team", "AI evaluation and red team"),
    "71": ("71-data-governance-privacy-retention", "Data governance privacy and retention"),
    "72": ("72-reference-implementation-golden-paths", "Reference implementation golden paths"),
    "73": ("73-system-builder-operating-manual", "System builder operating manual"),
    "74": ("74-dynamic-workspace-production-ux", "Dynamic workspace production UX"),
    "75": ("75-dynamic-workspace-certification", "Dynamic workspace certification"),
    "76": ("76-architecture-fitness-gate-pack", "Architecture fitness gate pack"),
    "77": ("77-canonical-data-message-governance", "Canonical data and message governance"),
    "78": ("78-canonical-data-dictionary-message-catalog", "Canonical data dictionary and message catalog"),
    "79": ("79-canonical-seed-catalog", "Canonical seed catalog"),
    "80": ("80-data-message-governance-cicd", "Data and message governance CI/CD"),
    "81": ("81-message-localization-knowledge-base", "Message localization and knowledge base"),
    "082": ("82-batch-run-governance", "Batch run governance"),
    "083": ("83-batch-operations-recovery", "Batch operations recovery"),
    "084": ("84-reporting-analytics-bi", "Reporting analytics and BI"),
    "085": ("85-report-generation-retention", "Report generation and retention"),
    "086": ("86-input-validation-data-integrity", "Input validation and data integrity"),
    "087": ("87-cross-layer-validation-implementation", "Cross-layer validation implementation"),
    "088": ("88-validation-error-feedback", "Validation error feedback"),
    "089": ("89-validation-evidence-testing", "Validation evidence and testing"),
    "090": ("90-enterprise-application-foundation", "Enterprise application foundation"),
    "090A": ("90-enterprise-application-foundation", "Enterprise application foundation"),
    "091": ("91-product-management-governance", "Product management governance"),
    "091-to-094": ("91-94-compliance-register-adoption", "Compliance register adoption"),
    "092": ("92-nfr-enterprise-readiness", "NFR enterprise readiness"),
    "094": ("94-enterprise-data-dictionary", "Enterprise data dictionary"),
    "095": ("95-register-adoption-source-pack", "Register adoption source pack"),
    "095A": ("95-register-adoption-source-pack", "Register adoption source pack"),
    "095B": ("95-register-adoption-source-pack", "Register adoption source pack"),
    "095C": ("95-register-adoption-source-pack", "Register adoption source pack"),
}


@dataclass(frozen=True)
class DocMeta:
    source_name: str
    doc_id: str
    title: str
    version: str
    status: str
    folder: str
    category: str
    slug: str


def text_of(node: ET.Element) -> str:
    chunks: list[str] = []
    for child in node.iter():
        if child.tag == f"{{{NS['w']}}}t":
            chunks.append(child.text or "")
        elif child.tag == f"{{{NS['w']}}}tab":
            chunks.append("\t")
        elif child.tag == f"{{{NS['w']}}}br":
            chunks.append("\n")
    return "".join(chunks).strip()


def paragraph_style(paragraph: ET.Element) -> str:
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    return style.attrib.get(f"{{{NS['w']}}}val", "") if style is not None else ""


def paragraph_to_markdown(paragraph: ET.Element) -> str:
    text = text_of(paragraph)
    if not text:
        return ""

    style = paragraph_style(paragraph).lower()
    heading_match = re.search(r"heading([1-6])", style)
    if heading_match:
        level = int(heading_match.group(1))
        return f"{'#' * level} {text}"

    return text


def table_to_markdown(table: ET.Element) -> list[str]:
    rows: list[list[str]] = []
    for row in table.findall("./w:tr", NS):
        cells = []
        for cell in row.findall("./w:tc", NS):
            cell_text = " ".join(
                text_of(paragraph)
                for paragraph in cell.findall("./w:p", NS)
                if text_of(paragraph)
            )
            cells.append(cell_text.replace("|", "\\|"))
        if cells:
            rows.append(cells)

    if not rows:
        return []

    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    header = normalized[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def iter_body_blocks(root: ET.Element) -> Iterable[str]:
    body = root.find("w:body", NS)
    if body is None:
        return
    for child in body:
        if child.tag == f"{{{NS['w']}}}p":
            markdown = paragraph_to_markdown(child)
            if markdown:
                yield markdown
        elif child.tag == f"{{{NS['w']}}}tbl":
            for line in table_to_markdown(child):
                yield line


def parse_metadata(source_name: str) -> DocMeta:
    stem = Path(source_name).stem
    match = re.match(
        r"^(AIRA_[0-9]{2,3}(?:_to_[0-9]{2,3})?[A-Z]?|AIRA-DOC-[0-9]{3}[A-Z]?)[_-](.+?)_v([0-9]+(?:[._][0-9]+)*)(?:_|$)",
        stem,
    )
    if not match:
        raise ValueError(f"Cannot parse metadata from {source_name}")

    raw_id, raw_title, raw_version = match.groups()
    doc_id = raw_id.replace("_", "-")
    short_id = doc_id.replace("AIRA-", "").replace("DOC-", "")
    version = "v" + raw_version.replace("_", ".")
    status = "draft" if "Draft" in stem else "revised" if "Revised" in stem else "final"
    title = raw_title.replace("_", " ")
    folder, category = CATEGORIES.get(short_id, ("99-unsorted", "Unsorted"))
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return DocMeta(source_name, doc_id, title, version, status, folder, category, slug)


def yaml_scalar(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def frontmatter(meta: DocMeta) -> str:
    tags = [
        "aira",
        meta.folder,
        meta.status,
        meta.doc_id.lower().replace("-", "-"),
    ]
    today = date.today().isoformat()
    lines = [
        "---",
        f"title: {yaml_scalar(meta.title)}",
        f"doc_id: {yaml_scalar(meta.doc_id)}",
        f"version: {yaml_scalar(meta.version)}",
        f"status: {yaml_scalar(meta.status)}",
        f"category: {yaml_scalar(meta.category)}",
        f"source_docx: {yaml_scalar(meta.source_name)}",
        f"converted_on: {yaml_scalar(today)}",
        "tags:",
    ]
    lines.extend(f"  - {tag}" for tag in tags)
    lines.append("---")
    return "\n".join(lines)


def convert_docx(source: Path, destination: Path, meta: DocMeta) -> None:
    with zipfile.ZipFile(source) as docx:
        document_xml = docx.read("word/document.xml")
    root = ET.fromstring(document_xml)
    body = list(iter_body_blocks(root))

    content = [frontmatter(meta), "", f"# {meta.title}", ""]
    if body:
        first = body[0].lstrip("# ").strip().lower()
        if first != meta.title.lower():
            content.extend(body)
        else:
            content.extend(body[1:])
    content.append("")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n\n".join(content).replace("\n\n|", "\n|").replace("|\n\n|", "|\n|"), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert first-batch AIRA DOCX files to Obsidian Markdown.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()

    missing: list[str] = []
    generated: list[Path] = []
    for source_name in SOURCE_FILES:
        source = args.source / source_name
        if not source.exists():
            missing.append(source_name)
            continue
        meta = parse_metadata(source_name)
        destination = args.target / meta.folder / f"{meta.slug}.md"
        convert_docx(source, destination, meta)
        generated.append(destination)

    if missing:
        raise SystemExit("Missing source files:\n" + "\n".join(missing))

    print(f"Generated {len(generated)} Markdown files.")
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
