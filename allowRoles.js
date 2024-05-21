// Middleware to allow only specific roles
const allowRoles = (users, roles) => {
    return (req, res, next) => {
        const user = users.find((u) => u.id === req.user.userId);
        if (!roles.includes(user.role)) {
            return res.status(403).json({ message: "Unauthorized" });
        }
        next();
    };
};

module.exports = allowRoles;
