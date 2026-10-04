# Workroom working contract

The design authority is [design-profile.md](design-profile.md), with supplied owner evidence in [OWNER.md](OWNER.md).

Approved requirement `task-update`: members find and update their assigned task with understandable state and recovery. This is product intent, not proof of an implementation. Task list/detail/comments and the existing administrator surface are in scope. No new backend or role.

Read the existing `tools/profile_reader.py` consumer before migrating that path. Token values belong to [ui-tokens.json](ui-tokens.json); runtime storage and frontend consumers are not supplied.
